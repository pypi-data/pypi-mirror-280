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
"""Servicer for FlowerService.

Relevant knowledge for reading this modules code:
    - https://github.com/grpc/grpc/blob/master/doc/statuscodes.md
"""
from contextlib import contextmanager
from typing import Callable, Iterator, Any, Dict, Tuple, Optional
import grpc
from iterators import TimeoutIterator

from daisyflcocdrlib.proto import transport_pb2_grpc
from daisyflcocdrlib.proto.transport_pb2 import ClientMessage, ServerMessage
from daisyflcocdrlib.common.logger import log
from logging import INFO, WARNING, DEBUG, ERROR
from daisyflcocdrlib.common import (
    serde,  
    Code,
    ServerReceivedSignal,
    Status,
    ModelSyncMessage,
    ModelTransferReservation,
    ReservationSuccess,
    ReservationFailure,
)
import time

class ClientServiceServicer(transport_pb2_grpc.FlowerServiceServicer):
    """FlowerServiceServicer for bi-directional gRPC message stream."""

    def __init__(
        self,
        server_address: str,
    ) -> None:
        self.server_address: str = server_address
        
    def set_model_sync_fn(self, model_sync_fn: Callable):
        self.model_sync_fn: Callable = model_sync_fn

    def set_shutdown_fn(self, shutdown_fn: Callable):
        self.shutdown_fn: Callable = shutdown_fn
    
    def set_reservation_fn(self, reservation_fn: Callable):
        self.reservation_fn = reservation_fn
        
    def Join(  # pylint: disable=invalid-name
        self,
        request_iterator: Iterator[ClientMessage],
        context: grpc.ServicerContext,
    ) -> Iterator[ServerMessage]:
        """Method will be invoked by each GrpcClientProxy which participates in
        the network.

        Protocol:
            ...
            - The Join method is (pretty much) protocol unaware
        """
        # process Iterator
        client_timeout_iterator = TimeoutIterator(iterator=request_iterator, reset_on_next=True)
        client_message, success = self.get_client_message(client_message_iterator=client_timeout_iterator, context=context,)
        if not success:
            return
        field = client_message.WhichOneof("msg")
        if field == "model_sync_request":
            model_sync_message: ModelSyncMessage = serde.model_sync_request_from_proto(client_message.model_sync_request)
            yield from self.model_sync(model_sync_message=model_sync_message)
            _, _ = self.get_client_message(client_message_iterator=client_timeout_iterator, context=context,)
            log(WARNING, "RxDev, send_model: gRPCServer disconnect. This shouldn't happen")
        elif field == "model_transfer_reservation":
            model_transfer_reservation: ModelTransferReservation = serde.model_transfer_reservation_from_proto(client_message.model_transfer_reservation)
            yield from self.reservation(model_transfer_reservation)
            # wait for client disconnection
            _, _ = self.get_client_message(client_message_iterator=client_timeout_iterator, context=context,)
            log(WARNING, "RxDev, reservation: gRPCServer disconnect. This shouldn't happen")
        elif field == "shutdown":
            self.shutdown()
            return
        else:
            log(ERROR, "Receive unexpected message type.")
            return
    
    # process different message types
    def model_sync(self, model_sync_message: ModelSyncMessage):
        try:
            # set model
            self.model_sync_fn(model_sync_message)
            log(DEBUG, "RxDev, send_model: set ModelSyncMessage")
            # send SRS
            srs = ServerReceivedSignal(status=Status(code=Code.OK, message=""))
            server_message = ServerMessage(server_received_signal=serde.server_received_signal_to_proto(srs))
            yield server_message
            log(DEBUG, "RxDev, send_model: send SRS")
        except StopIteration:
            return

    def reservation(self, model_transfer_reservation: ModelTransferReservation):
        try:
            success = self.reservation_fn(model_transfer_reservation)
            if success:
                rs_proto = serde.reservation_success_to_proto(ReservationSuccess(status=""))
                sm = ServerMessage(reservation_success=rs_proto)
                yield sm
                log(WARNING, "RxDev, reservation: Send ReservationSuccess")
            else:
                rf_proto = serde.reservation_failure_to_proto(ReservationFailure(status=""))                
                yield ServerMessage(reservation_failure=rf_proto)
                log(WARNING, "RxDev, reservation: Send ReservationFailure")
        except StopIteration:
            return

    def shutdown(self,):
        self.shutdown_fn()
        return

    # communication
    def get_client_message(self, client_message_iterator: TimeoutIterator,  context: grpc.ServicerContext, timeout: Optional[int] = None,) -> Tuple[ClientMessage, bool]:
        log(DEBUG, "Try receiving ClientMessage")
        if timeout is not None:
            client_message_iterator.set_timeout(float(timeout))
        # Wait for client message
        client_message = next(client_message_iterator)
        if client_message is client_message_iterator.get_sentinel():
            # Important: calling `context.abort` in gRPC always
            # raises an exception so that all code after the call to
            # `context.abort` will not run. If subsequent code should
            # be executed, the `rpc_termination_callback` can be used
            # (as shown in the `register_client` function).
            details = f"Timeout of {timeout}sec was exceeded."
            context.abort(
                code=grpc.StatusCode.DEADLINE_EXCEEDED,
                details=details,
            )
            # This return statement is only for the linter so it understands
            # that client_message in subsequent lines is not None
            # It does not understand that `context.abort` will terminate
            # this execution context by raising an exception.
            return client_message, False
        return client_message, True

