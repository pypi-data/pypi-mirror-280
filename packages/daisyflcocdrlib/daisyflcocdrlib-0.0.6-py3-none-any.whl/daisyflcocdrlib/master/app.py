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
"""Flower server app."""
from logging import INFO, WARN, ERROR
from typing import Optional, Tuple, Dict, Callable, List

from daisyflcocdrlib.common.logger import log
from daisyflcocdrlib.common import (
    Type,
    GRPC_MAX_MESSAGE_LENGTH,
)
from daisyflcocdrlib.proto.transport_pb2_grpc import add_FlowerServiceServicer_to_server
from daisyflcocdrlib.utils.client_manager import SimpleClientManager
from daisyflcocdrlib.master.grpc_server.grpc_server import (
    generic_create_grpc_server,
    start_grpc_server,
)
from daisyflcocdrlib.utils.server import Server
from daisyflcocdrlib.utils.server_operator_manager import ServerOperatorManager
from daisyflcocdrlib.utils.task_manager import TaskManager
from daisyflcocdrlib.master.server_api_handler import ServerListener

import threading
import time

DEFAULT_SERVER_ADDRESS = "[::]:8887"
_cnd_stop: threading.Condition = threading.Condition()
def shutdown():
    with _cnd_stop:
        _cnd_stop.notify()

def start_master(  # pylint: disable=too-many-arguments
    *,
    # server
    server_address: str = DEFAULT_SERVER_ADDRESS,
    # api_handler
    api_ip: str = None,
    api_port: int = None,
    # grpc
    grpc_max_message_length: int = GRPC_MAX_MESSAGE_LENGTH,
    certificates: Optional[Tuple[bytes, bytes, bytes]] = None,
) -> None:
    # Initialize server and task manager
    initialized_server: Server = _init_defaults(
        server_address=server_address,
        api_ip=api_ip,
        api_port=api_port,
    )
    log(INFO, "Starting Master server",)

    # Start gRPC server
    grpc_server = start_grpc_server(
        client_manager=initialized_server.get_client_manager(),
        server_address=server_address,
        max_message_length=grpc_max_message_length,
        certificates=certificates,
        chain_transfer_fn=initialized_server.chain_transfer_fn,
        model_sync_fn=initialized_server.server_sync_fn,
        shutdown_fn=shutdown,
    )
    log(
        INFO,
        "Master gRPC server running , SSL is %s",
        "enabled" if certificates is not None else "disabled",
    )

    # Wait until shutdown
    with _cnd_stop:
        _cnd_stop.wait()
    # Stop the gRPC server
    grpc_server.stop(grace=1)
    initialized_server.get_client_manager().unregister_all()
    log(INFO, "Master server shutdown")
    exit(0)


def _init_defaults(
    server_address: str,
    api_ip: str = None,
    api_port: int = None,
) -> Server:
    # client_manager
    client_manager = SimpleClientManager()       
    # server
    server = Server(client_manager=client_manager, server_address=server_address,)
    # server_operator_manager
    server_operator_manager = ServerOperatorManager(server=server)
    # task_manager
    task_manager = TaskManager(
        server_operator_manager=server_operator_manager,
        manager_type=Type.MASTER,
    )
    # start ServerListener
    start_server_listener(api_ip=api_ip, api_port=api_port, task_manager=task_manager)
    
    return server

# server_listener
def start_server_listener(api_ip: str, api_port: int, task_manager: TaskManager) -> bool:
    if isinstance(api_ip, str) and isinstance(api_port, int):
        listener = ServerListener(api_ip, api_port, task_manager,)
        listener_thread = threading.Thread(target=listener.run, args=())
        listener_thread.setDaemon(True)
        listener_thread.start()
        time.sleep(1)
        if not listener_thread.is_alive():
            log(ERROR, "ServerListner failed")
            exit(1)
    else:
        log(
            ERROR,
            "Please check api_ip is string and api_port is integer.",
        )
        exit(1)
    return True
