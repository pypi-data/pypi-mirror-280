# Copyright 2020 Adap GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Flower server."""


import concurrent.futures
import timeit
from threading import Event, Condition, Lock, Timer, Thread
from queue import Queue
from logging import DEBUG, INFO, WARNING, ERROR
from typing import Dict, List, Optional, Tuple, Union, Callable
import gc
from daisyflcocdrlib.common import (
    Task,
    Report,
    CURRENT_ROUND,
    EVALUATE,
    TIMEOUT,
    FIT_SAMPLES,
    EVALUATE_SAMPLES,
    LOSS,
    METRICS,
    Code,
    DisconnectRes,
    EvaluateIns,
    EvaluateRes,
    FitIns,
    FitRes,
    Parameters,
    ReconnectIns,
    Scalar,
    CurrentReturns,
    TID,
    CID,
    ROAMING_TIMEOUT,
    IS_ROAMER,
    CREDENTIAL,
    ModelSyncMessage,
    serde,
    ChainTransferSignal,
    ChainProceedingSignal,
)
from daisyflcocdrlib.common.logger import log
from daisyflcocdrlib.common.typing import GetParametersIns
from daisyflcocdrlib.utils.client_manager import ClientManager
from daisyflcocdrlib.utils.client_proxy import ClientProxy
from daisyflcocdrlib.utils.criterion import Criterion
from daisyflcocdrlib.utils.model_sync import send_model

FitResultsAndFailures = Tuple[
    List[Tuple[ClientProxy, FitRes]],
    List[Union[Tuple[ClientProxy, FitRes], BaseException]],
]
EvaluateResultsAndFailures = Tuple[
    List[Tuple[ClientProxy, EvaluateRes]],
    List[Union[Tuple[ClientProxy, EvaluateRes], BaseException]],
]
ReconnectResultsAndFailures = Tuple[
    List[Tuple[ClientProxy, DisconnectRes]],
    List[Union[Tuple[ClientProxy, DisconnectRes], BaseException]],
]

class Find(Criterion):
    def __init__(self, cid: str):
        self.cid = cid

    def select(self, client: ClientProxy) -> bool:
        if client.cid == self.cid:
            return True
        return False

class SubtaskManager:
    def __init__(self,) -> None:
        self.subtasks: Dict[int, CurrentReturns] = {}
        self.queues: Dict[int, Queue] = {}
        self.roaming_queues_fit: Dict[str, Queue[FitRes, int, float]] = {} # {"tid": Queue[res, timeout, time_stamp]}
        self.roaming_queues_evaluate: Dict[str, Queue[EvaluateRes, int, float]] = {} # {"tid": Queue[res, timeout, time_stamp]}
        self.client_previous_subtask: Dict[str, int] = {}
        self.timeouts: Dict[int, List] = {} # [TIMEOUT, start_time] 
        self.edge_model_buf: Dict[str, List(ModelSyncMessage)] = {}
        self._generator_lock: Lock = Lock()
        self._server_sync_lock: Lock = Lock()
        self._roaming_lock: Lock = Lock()
        self._subtask_num = 0
        self.scheduler = Thread(target=self.check_timeout, args=())
        self.scheduler.setDaemon(True)
        self.scheduler.start()
    
    def subtask_id_generator(self,) -> int:
        with self._generator_lock:
            tmp = self._subtask_num
            self._subtask_num += 1
        return tmp

    def check_timeout(self,) -> None:
        while(1):
            running_subtasks = list(self.timeouts.keys())
            for i in running_subtasks:
                try:
                    current = timeit.default_timer()
                    if current - self.timeouts[i][1] > self.timeouts[i][0]:
                        self.unregister_subtask(i)
                except:
                    pass
            with self._roaming_lock:
                task_keys = list(self.roaming_queues_fit.keys())
                for k in task_keys:
                    try:
                        current = timeit.default_timer()
                        ql = self.roaming_queues_fit[k].qsize()
                        for _ in range(ql):
                            res, timeout, time_stamp = self.roaming_queues_fit[k].get()
                            if current - time_stamp <= timeout:
                                self.roaming_queues_fit[k].put((res, timeout, time_stamp))
                    except:
                        pass
                task_keys = list(self.roaming_queues_evaluate.keys())
                for k in task_keys:
                    try:
                        current = timeit.default_timer()
                        ql = self.roaming_queues_evaluate[k].qsize()
                        for _ in range(ql):
                            res, timeout, time_stamp = self.roaming_queues_evaluate[k].get()
                            if current - time_stamp <= timeout:
                                self.roaming_queues_evaluate[k].put((res, timeout, time_stamp))
                    except:
                        pass
            gc.collect()
            Event().wait(timeout=600)
    
    def register_subtask(
        self, subtask_id: int, 
        client_instructions: List[Tuple[ClientProxy, FitIns]],
        timeout: int,
    ) -> None:
        # CurrentReturns
        self.subtasks[subtask_id]: CurrentReturns = CurrentReturns(
            selected=len(client_instructions),
            results_num=0,
            failures_num=0,
            roaming_num=0,
            cnd=Condition(),
        )
        # queue
        self.queues[subtask_id] = Queue()
        # timeout
        self.timeouts[subtask_id] = [timeout, timeit.default_timer()]
        # update client_previoud_subtask
        for item in client_instructions:
            cid = item[0].cid
            if self.client_previous_subtask.__contains__(cid):
                pre_subtask = self.client_previous_subtask[cid]
                self.subtasks[pre_subtask].failures_num += 1
                del self.client_previous_subtask[cid]
                self.subtasks[pre_subtask].cnd.notify_all()
            self.client_previous_subtask[cid] = subtask_id

    def unregister_subtask(self, subtask_id: int) -> None:
        del self.subtasks[subtask_id]
        del self.queues[subtask_id]
        del self.timeouts[subtask_id]
        cid_list = list(self.client_previous_subtask.keys())
        for cid in cid_list:
            if self.client_previous_subtask[cid] == subtask_id:
                del self.client_previous_subtask[cid]
        return

    def check_waiting(self, cid: str) -> bool:
        if self.client_previous_subtask.__contains__(cid):
            return True
        return False

    def submit_subtask(
        self, result: Tuple[ClientProxy, Union[FitRes, EvaluateRes]], roaming=False,
    ) -> None:
        client_proxy, res = result
        if roaming:
            if res.status.code == Code.OK:
                result[1].config[CID] = result[0].cid
                tid = res.config[TID]
                roaming_timeout = res.config[ROAMING_TIMEOUT]
                res.config[IS_ROAMER] = True
                with self._roaming_lock:
                    if isinstance(res, FitRes):
                        if not self.roaming_queues_fit.__contains__(tid):
                            self.roaming_queues_fit[tid] = Queue()
                        self.roaming_queues_fit[tid].put((result, roaming_timeout, timeit.default_timer()))
                    else:
                        if not self.roaming_queues_evaluate.__contains__(tid):
                            self.roaming_queues_evaluate[tid] = Queue()
                        self.roaming_queues_evaluate[tid].put((result, roaming_timeout, timeit.default_timer()))
        else:
            if (not self.client_previous_subtask.__contains__(client_proxy.cid)):
                return
            subtask_id = self.client_previous_subtask[client_proxy.cid]
            if (not self.subtasks.__contains__(subtask_id)):
                return
            # Check result status code
            if res.status.code == Code.OK:
                result[1].config[CID] = result[0].cid
                self.subtasks[subtask_id].results_num += 1
                self.queues[subtask_id].put(result)
            # Not successful, client returned a result where the status code is not OK
            else:
                self.subtasks[subtask_id].failures_num += 1
            del self.client_previous_subtask[client_proxy.cid]
            with self.subtasks[subtask_id].cnd:
                self.subtasks[subtask_id].cnd.notify_all()
            return
        
    def client_fail(self, cid: str) -> None:
        if (not self.client_previous_subtask.__contains__(cid)):
            return
        subtask_id = self.client_previous_subtask[cid]
        if (not self.subtasks.__contains__(subtask_id)):
            return
        self.subtasks[subtask_id].failures_num += 1
        del self.client_previous_subtask[cid]
        with self.subtasks[subtask_id].cnd:
            self.subtasks[subtask_id].cnd.notify_all()
        return
    
    def client_roam(self, cid: str) -> None:
        if (not self.client_previous_subtask.__contains__(cid)):
            return
        subtask_id = self.client_previous_subtask[cid]
        if (not self.subtasks.__contains__(subtask_id)):
            return
        self.subtasks[subtask_id].roaming_num += 1
        del self.client_previous_subtask[cid]
        with self.subtasks[subtask_id].cnd:
            self.subtasks[subtask_id].cnd.notify_all()
        return
    
    def chain_transfer_fn(self, cid: str, cts: ChainTransferSignal) -> None:
        subtask_id = self.client_previous_subtask[cid]
        del self.client_previous_subtask[cid]
        self.client_previous_subtask[cts.transfer_to] = subtask_id
        return

    def server_sync_fn(self, server_sync_message: ModelSyncMessage) -> bool:
        with self._server_sync_lock:
            if not server_sync_message.config.__contains__(TID):
                log(WARNING, "Ignore an edge model without task ID. Please send it with a key of \"TID\" in the dictionary")
                return False
            if not self.edge_model_buf.__contains__(server_sync_message.config[TID]):
                self.edge_model_buf[server_sync_message.config[TID]] = []
            self.edge_model_buf[server_sync_message.config[TID]].append(server_sync_message)
            return True
    
    def get_server_sync_message(self, tid: str) -> List[ModelSyncMessage]:
        with self._server_sync_lock:
            if not self.edge_model_buf.__contains__(tid):
                return []
            else:
                tmp = self.edge_model_buf[tid]
                self.edge_model_buf[tid] = []
                return tmp

    def get_current_returns(self, subtask_id: int) -> CurrentReturns:
        return self.subtasks[subtask_id]
    
    def get_results(self, subtask_id: int) -> List[Tuple[ClientProxy, Union[FitRes, EvaluateRes]]]:
        results = []
        q = self.queues[subtask_id]
        for _ in range(q.qsize()):
            results.append(q.get())
        return results
    
    def get_results_roaming(self, tid: str, fit: bool=True) -> List[Tuple[ClientProxy, Union[FitRes, EvaluateRes]]]:
        with self._roaming_lock:
            results = []
            if fit:
                if not self.roaming_queues_fit.__contains__(tid):
                    return []
                q = self.roaming_queues_fit[tid]
            else:
                if not self.roaming_queues_evaluate.__contains__(tid):
                    return []
                q = self.roaming_queues_evaluate[tid]
            for _ in range(q.qsize()):
                result, _, _ = q.get()
                results.append(result)
            return results


class Server:
    """Flower server."""
    def __init__(
        self, *, 
        client_manager: ClientManager,
        server_address: str,
    ) -> None:
        self.server_address: str = server_address
        self._client_manager: ClientManager = client_manager
        self._max_workers: Optional[int] = None
        self._subtask_manager: SubtaskManager = SubtaskManager()
        self._client_manager.set_submit_subtask_fn(self._subtask_manager.submit_subtask)
        self._client_manager.set_check_waiting_fn(self._subtask_manager.check_waiting)
        self._client_manager.set_client_fail_fn(self._subtask_manager.client_fail)
        self._client_manager.set_client_roam_fn(self._subtask_manager.client_roam)

    # set Server attributes
    def set_max_workers(self, max_workers: Optional[int]) -> None:
        """Set the max_workers used by ThreadPoolExecutor."""
        self._max_workers = max_workers

    # get Server attributes
    def get_client_manager(self) -> ClientManager:
        """Return ClientManager."""
        return self._client_manager

    def get_max_workers(self) -> Optional[int]:
        """Return max_workers."""
        return self._max_workers
    
    # NOTE: ClientManager APIs 
    def num_available(self, credential: Optional[str] = None) -> int:
        return self._client_manager.num_available(credential=credential)
        
    def sample(
        self,
        num_clients: int,
        min_num_clients: Optional[int] = None,
        credential: Optional[str] = None,
        criterion: Optional[Criterion] = None,
    ) -> List[ClientProxy]:
        return self._client_manager.sample(
            num_clients=num_clients,
            min_num_clients=min_num_clients,
            credential=credential,
            criterion=criterion,
        )
    
    def get_clients_from_list(
        self,
        clients: List[Tuple[ClientProxy, Union[FitIns, EvaluateIns]]],
        timeout: float,
        credential: str,
    ) -> List[Tuple[ClientProxy, Union[FitIns, EvaluateIns]]]:
        ids = []
        client_list = []
        instructions = []
        for client, ins in clients:
            ids.append(client.cid)
            client_list.append(client)
            instructions.append(ins)
        client_list = self._client_manager.get_clients_from_list(clients=client_list, timeout=timeout, credential=credential,)
        available_clients_and_ins = []
        for client in client_list:
            available_clients_and_ins.append((client, instructions[ids.index(client.cid)]))
        return available_clients_and_ins

    # NOTE: SubtaskManager APIs
    def finish_subtask(self, subtask_id: int) -> None:
        self._subtask_manager.unregister_subtask(subtask_id)

    def get_current_returns(self, subtask_id: int) -> CurrentReturns:
        return self._subtask_manager.get_current_returns(subtask_id)
    
    def get_results(self, subtask_id: int) -> List[Tuple[ClientProxy, Union[FitRes, EvaluateRes]]]:
        return self._subtask_manager.get_results(subtask_id)
    
    def get_results_roaming(self, tid: str, fit: bool=True) -> List[Tuple[ClientProxy, Union[FitRes, EvaluateRes]]]:
        return self._subtask_manager.get_results_roaming(tid=tid, fit=fit)

    def get_server_sync_message(self, tid: str) -> List[ModelSyncMessage]:
        return self._subtask_manager.get_server_sync_message(tid=tid)

    def synchronize_edge_model(self, dest: str, model_sync_message: ModelSyncMessage) -> None:
        if not model_sync_message.config.__contains__(TID):
            log(WARNING, "Ignore an edge model without task ID. Please send it with a key of \"TID\" in the dictionary")
            return
        send_model(dest=dest, model_sync_message=model_sync_message)
        return
    
    def server_sync_fn(self, server_sync_message: ModelSyncMessage):
        self._subtask_manager.server_sync_fn(server_sync_message)
        return

    def chain_transfer_fn(self, cid: str, credential: str, cts: ChainTransferSignal):
        self._subtask_manager.chain_transfer_fn(cid, cts)
        # TODO: send message
        cps = ChainProceedingSignal(config=cts.config)
        criterion = Find(cts.transfer_to)
        for trials in range(10):
            clients = self.sample(num_clients=1, min_num_clients=1, credential=credential,criterion=criterion)
            if len(clients) == 0:
                # Selection Failure
                log(WARNING, "Can't find the objective client_proxy.")
                Event().wait(timeout=3)
            else:
                # Selection Success
                clients[0].fit(cps)
                return

    # TODO:
    def disconnect_all_clients(self,) -> None:
        """Send shutdown signal to all clients."""
        clients = self.get_client_manager().all() 
        instruction = ReconnectIns(seconds=None)
        client_instructions = [(client_proxy, instruction) for client_proxy in clients]
        _ = self._reconnect_clients(
            client_instructions=client_instructions,
            max_workers=self.get_max_workers(),
        )

    def fit_clients(
        self,
        client_instructions: List[Tuple[ClientProxy, FitIns]],
        max_workers: Optional[int],
        timeout: Optional[float],
    ) -> int:
        subtask_id = self._subtask_manager.subtask_id_generator()
        self._subtask_manager.register_subtask(subtask_id, client_instructions, timeout)
        self._fit_clients(
            client_instructions=client_instructions,
            max_workers=max_workers,
        )
        return subtask_id
    
    def evaluate_clients(
        self,
        client_instructions: List[Tuple[ClientProxy, EvaluateIns]],
        max_workers: Optional[int],
        timeout: Optional[float],
    ) -> int:
        subtask_id = self._subtask_manager.subtask_id_generator()
        self._subtask_manager.register_subtask(subtask_id, client_instructions, timeout)
        self._evaluate_clients(
            client_instructions=client_instructions,
            max_workers=max_workers,
        )
        return subtask_id


    def _reconnect_clients(
        self,
        client_instructions: List[Tuple[ClientProxy, ReconnectIns]],
        max_workers: Optional[int],
    ) -> ReconnectResultsAndFailures:
        """Instruct clients to disconnect and never reconnect."""
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            submitted_fs = {
                executor.submit(self._reconnect_client, self, client_proxy, ins,)
                for client_proxy, ins in client_instructions
            }
            finished_fs, _ = concurrent.futures.wait(
                fs=submitted_fs,
                timeout=None,  # Handled in the respective communication stack
            )

        # Gather results
        results: List[Tuple[ClientProxy, DisconnectRes]] = []
        failures: List[Union[Tuple[ClientProxy, DisconnectRes], BaseException]] = []
        for future in finished_fs:
            failure = future.exception()
            if failure is not None:
                failures.append(failure)
            else:
                result = future.result()
                results.append(result)
        return results, failures


    def _reconnect_client(
        self,
        client: ClientProxy,
        reconnect: ReconnectIns,
        timeout: Optional[float],
    ) -> Tuple[ClientProxy, DisconnectRes]:
        """Instruct client to disconnect and (optionally) reconnect later."""
        disconnect = client.reconnect(
            reconnect,
            timeout=timeout,
        )
        return client, disconnect


    def _fit_clients(
        self,
        client_instructions: List[Tuple[ClientProxy, FitIns]],
        max_workers: Optional[int],
    ) -> None:
        """Refine parameters concurrently on all selected clients."""
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            {
                executor.submit(client_proxy.fit, ins,)
                for client_proxy, ins in client_instructions
            }


    def _evaluate_clients(
        self,
        client_instructions: List[Tuple[ClientProxy, EvaluateIns]],
        max_workers: Optional[int],
    ) -> None:
        """Evaluate parameters concurrently on all selected clients."""
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            {
                executor.submit(client_proxy.evaluate, ins,)
                for client_proxy, ins in client_instructions
            }

