from logging import DEBUG, INFO, ERROR, WARNING
from daisyflcocdrlib.common.logger import log
from dataclasses import dataclass
from typing import List, Tuple, Union
from daisyflcocdrlib.utils import dynamic_load
from daisyflcocdrlib.operator.base.client_logic import ClientLogic
from daisyflcocdrlib.common import (
    Parameters,
    Task,
    Report,
    FitIns,
    FitRes,
    ChainProceedingSignal,
    ChainTransferSignal,
    EvaluateIns,
    EvaluateRes,
    ModelSyncMessage,
    TID,
    REMOVE_OPERATOR,
    OPERATORS,
    STRATEGIES,
    CLIENT_OPERATOR,
    ModelTransferReservation,
)

from daisyflcocdrlib.client.client import Client

@dataclass
class TaskOperator:
    tid: str
    operator_path: List[str]
    operator: ClientLogic

# TODO: release locks before shutdown

class ClientOperatorManager:
    def __init__(self, client: Client, server_address: str):
        self.client: Client = client
        self.server_address = server_address
        self.operators: List[TaskOperator] = []
        self._connector = None
        self.operator_key = CLIENT_OPERATOR

    def disconnect(self) -> None:
        # TODO:
        pass

    def fit(
        self, ins: Union[FitIns, ChainProceedingSignal],
    ) -> Union[FitRes, ChainTransferSignal]:
        task_operator = self._get_task_operator(tid=ins.config[TID])
        if not task_operator:
            self._register_operator(
                tid=ins.config[TID],
                operator_path=ins.config[OPERATORS][self.operator_key],
            )
            task_operator = self._get_task_operator(tid=ins.config[TID])
        if (task_operator.operator_path != ins.config[OPERATORS][self.operator_key]):
            log(WARNING, "Operator changed.")
            self._unregister_operator(tid=ins.config[TID])
            self._register_operator(
                tid=ins.config[TID],
                operator_path=ins.config[OPERATORS][self.operator_key],
            )

        res: Union[FitRes, ChainTransferSignal] = task_operator.operator.fit(ins)

        # if ins.config.__contains__(REMOVE_OPERATOR):
        #     if ins.config[REMOVE_OPERATOR]:
        #         self._unregister_operator(tid=ins.config[TID])

        return res

    def evaluate(
        self, ins: EvaluateIns,
    ) -> EvaluateRes:
        task_operator = self._get_task_operator(tid=ins.config[TID])

        if not task_operator:
            self._register_operator(
                tid=ins.config[TID],
                operator_path=ins.config[OPERATORS][self.operator_key],
            )
            task_operator = self._get_task_operator(tid=ins.config[TID])
        if (task_operator.operator_path != ins.config[OPERATORS][self.operator_key]):
            log(WARNING, "Operator changed.")
            self._unregister_operator(tid=ins.config[TID])
            self._register_operator(
                tid=ins.config[TID],
                operator_path=ins.config[OPERATORS][self.operator_key],
            )

        res: FitRes = task_operator.operator.evaluate(ins)
        
        # if ins.config.__contains__(REMOVE_OPERATOR):
        #     if ins.config[REMOVE_OPERATOR]:
        #         self._unregister_operator(tid=ins.config[TID])

        return res 

    # APIs
    def model_sync_fn(self, msm: ModelSyncMessage):
        if not msm.config.__contains__(TID):
            log(WARNING, "Ignore an client model without task ID. Please send it with a key of \"TID\" in the dictionary")
            return
        task_operator = self._get_task_operator(msm.config[TID])
        if task_operator is None:
            log(WARNING, "Can't find the operator corresponding to the task ID of the client model")
            log(INFO, "register a client operator")
            self._register_operator(
                tid=msm.config[TID],
                operator_path=msm.config[OPERATORS][self.operator_key],
            )
            task_operator = self._get_task_operator(tid=msm.config[TID])
        task_operator.operator.c2c_model_sync(msm)
        return

    def reservation_fn(self, mtr: ModelTransferReservation) -> bool:
        if not mtr.config.__contains__(TID):
            log(WARNING, "Ignore an client model without task ID. Please send it with a key of \"TID\" in the dictionary")
            return False
        task_operator = self._get_task_operator(mtr.config[TID])
        if task_operator is None:
            log(WARNING, "Can't find the operator corresponding to the task ID of the client model")
            log(INFO, "register a client operator")
            self._register_operator(
                tid=mtr.config[TID],
                operator_path=mtr.config[OPERATORS][self.operator_key],
            )
            task_operator = self._get_task_operator(tid=mtr.config[TID])
        return task_operator.operator.reservation()

    def set_connector(self, connector) -> None:
        self._connector = connector

    def _get_task_operator(self, tid: str) -> TaskOperator:
        for task_operator in self.operators:
            if task_operator.tid == tid:
                return task_operator
        return None
    
    def _register_operator(self,
        tid: str,
        operator_path: List[str],
    ) -> bool:
        if self._get_task_operator(tid=tid):
            return False

        operator: ClientLogic = dynamic_load(operator_path[0], operator_path[1])
        op_instance = operator(client=self.client)
        op_instance.set_connector(self._connector)
        op_instance.set_address(self.server_address)

        self.operators.append(TaskOperator(
            tid=tid,
            operator_path=operator_path,
            operator=op_instance,
        ))

        return True
    
    def _unregister_operator(self, tid: str) -> bool:
        for i in range(len(self.operators)):
            if self.operators[i].tid == tid:
                self.operators[i].operator.unlock()
                del self.operators[i]
                return True
        return False

    def shutdown(self,):
        for i in range(len(self.operators)):
            self.operators[i].operator.unlock()

