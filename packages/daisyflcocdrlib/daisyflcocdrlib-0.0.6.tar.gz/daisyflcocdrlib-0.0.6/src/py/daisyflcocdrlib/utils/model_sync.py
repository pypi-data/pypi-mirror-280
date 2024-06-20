from daisyflcocdrlib.common.logger import log
from logging import INFO, WARNING, DEBUG, ERROR
from typing import Callable, Iterator, Any, Dict, Tuple, Optional
from daisyflcocdrlib.utils.connection import grpc_connection
from daisyflcocdrlib.common import (
    ModelSyncMessage,
    serde,
    ServerReceivedSignal,
    ModelTransferReservation,
    ReservationSuccess,
    ReservationFailure,
)
from daisyflcocdrlib.proto.transport_pb2 import ClientMessage, ServerMessage

def reservation(dest: str, mtr:ModelTransferReservation,) -> bool:
    try:
        # build connection
        with grpc_connection(
            parent_address=dest,
            metadata=(()),
            root_certificates=None
        ) as conn:
            send, receive = conn
            # send message
            cm = ClientMessage(model_transfer_reservation=serde.model_transfer_reservation_to_proto(mtr))
            send(cm)
            log(INFO, "TxDev, reservation: Send reservation message")
            # receive
            sm, _ = receive()
            field = sm.WhichOneof("msg")
            if field == "reservation_success":
                log(INFO, "TxDev, reservation: ReservationSuccess")
                return True
            elif field == "reservation_failure":
                log(INFO, "TxDev, reservation: ReservationFailure")
                return False
    except:
        log(WARNING, "TxDev, reservation: Connection Fail")
        return False

def send_model(
    dest: str,
    model_sync_message: ModelSyncMessage,
):
    try:
        # build connection
        with grpc_connection(
            parent_address=dest,
            metadata=(()),
            root_certificates=None
        ) as conn:
            send, receive = conn
            # send message
            msr = ClientMessage(model_sync_request=serde.model_sync_request_to_proto(request=model_sync_message))
            send(msr)
            log(WARNING, "TxDev, send_model: Send model")
            # receive SRS
            _, _ = receive()
            log(WARNING, "TxDev, send_model: Receive SRS")
        return
    except:
        log(WARNING, "TxDev, send_model: Connection Fail")
        return
