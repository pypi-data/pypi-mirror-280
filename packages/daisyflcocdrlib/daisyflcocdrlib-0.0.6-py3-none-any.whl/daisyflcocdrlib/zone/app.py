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
from logging import INFO, WARNING, ERROR
from typing import Optional, Tuple, Dict, Callable, List

from daisyflcocdrlib.common.logger import log
from daisyflcocdrlib.common import (
    Type,
    GRPC_MAX_MESSAGE_LENGTH,
    metadata_to_dict,
    dict_to_metadata,
    CID,
    CREDENTIAL,
    IS_ZONE,
)
from daisyflcocdrlib.proto.transport_pb2_grpc import add_FlowerServiceServicer_to_server
from daisyflcocdrlib.utils.client_manager import SimpleClientManager
from daisyflcocdrlib.zone.grpc_server.zone_service_servicer import ZoneServiceServicer
from daisyflcocdrlib.zone.grpc_server.grpc_server import (
    generic_create_grpc_server,
    start_grpc_server,
)
from daisyflcocdrlib.utils.history import History
from daisyflcocdrlib.utils.server import Server
from daisyflcocdrlib.utils.server_operator_manager import ServerOperatorManager
from daisyflcocdrlib.utils.task_manager import TaskManager
from daisyflcocdrlib.zone.grpc_client.z2m_connection import Z2MConnection
from daisyflcocdrlib.zone.zone_entry import ZoneEntry

import uuid
import threading
import time

DEFAULT_SERVER_ADDRESS = "[::]:8887"


def start_zone(  # pylint: disable=too-many-arguments
    *,
    parent_address: str = "",
    server_address: str = DEFAULT_SERVER_ADDRESS,
    grpc_max_message_length: int = GRPC_MAX_MESSAGE_LENGTH,
    certificates: Optional[Tuple[bytes, bytes, bytes]] = None,
) -> None:
    # Initialize server and task manager
    initialized_server, task_manager = _init_defaults(
        server_address=server_address,
    )

    # define zone metadata
    metadata_dict = metadata_to_dict(metadata=(), _check_required=False)
    metadata_dict[IS_ZONE] = "is_zone"
    if metadata_dict.__contains__(CREDENTIAL):
        log(WARNING, "CREDENTIAL is defined in the metadata of a zone. It will be ignored.")
        del metadata_dict[CREDENTIAL]
    if not metadata_dict.__contains__(CID):
        metadata_dict[CID] = str(uuid.uuid4())
    metadata = dict_to_metadata(metadata_dict)

    zone_entry = ZoneEntry(task_manager=task_manager)
    connector = Z2MConnection(
        parent_address=parent_address,
        max_message_length=grpc_max_message_length,
        metadata=metadata,
        zone_entry=zone_entry,
    )
    zone_entry.set_connector(connector=connector)

    log(INFO, "Starting Zone server",)
    # Start gRPC server
    grpc_server = start_grpc_server(
        client_manager=initialized_server.get_client_manager(),
        server_address=server_address,
        max_message_length=grpc_max_message_length,
        certificates=certificates,
        chain_transfer_fn=initialized_server.chain_transfer_fn,
        model_sync_fn=initialized_server.server_sync_fn,
        shutdown_fn=zone_entry.shutdown,
    )
    log(
        INFO,
        "Zone gRPC server running , SSL is %s",
        "enabled" if certificates is not None else "disabled",
    )

    ## C2ZConnection
    connector_thread = threading.Thread(target=connector.run, args=())
    connector_thread.setDaemon(True)
    connector_thread.start()
    ### check
    threading.Event().wait(timeout=1)
    if not connector_thread.is_alive():
        log(ERROR, "C2ZConnection failed")
        exit(1)
    ## ZoneEntry
    zone_entry.run()

    # Stop the gRPC server
    grpc_server.stop(grace=1)
    initialized_server.get_client_manager().unregister_all()
    log(INFO, "Zone server shutdown")
    exit(0)


def _init_defaults(
    server_address: str,
) -> Tuple[Server, TaskManager]:
    # client_manager
    client_manager = SimpleClientManager()       
    # server
    server = Server(client_manager=client_manager, server_address=server_address,)
    # server_operator_manager
    server_operator_manager = ServerOperatorManager(server=server)
    # task_manager
    task_manager = TaskManager(
        server_operator_manager=server_operator_manager,
        manager_type=Type.ZONE,
    )  
    
    return server, task_manager

