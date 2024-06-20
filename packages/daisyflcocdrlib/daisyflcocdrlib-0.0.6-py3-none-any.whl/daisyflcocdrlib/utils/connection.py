from contextlib import contextmanager
from typing import Callable, Iterator, Any, Dict, Tuple, Optional
import grpc
from iterators import TimeoutIterator
from daisyflcocdrlib.proto.transport_pb2 import ClientMessage, ServerMessage
from daisyflcocdrlib.common.logger import log
from logging import INFO, WARNING, DEBUG, ERROR
from daisyflcocdrlib.common import (
    GRPC_MAX_MESSAGE_LENGTH, 
    serde,
    Code,
    Status,
    FitRes,
    Parameters,
)
from daisyflcocdrlib.proto.transport_pb2_grpc import FlowerServiceStub
from queue import Queue

def on_channel_state_change(channel_connectivity: str) -> None:
    """Log channel connectivity."""
    log(DEBUG, channel_connectivity)

# sentinel
sentinel = ClientMessage(fit_res=serde.fit_res_to_proto(FitRes(
    status=Status(code=Code.OK, message="Success"),
    parameters=Parameters(tensors=[], tensor_type=""),
    config={},
)))
    
@contextmanager
def grpc_connection(
    parent_address: str,
    metadata: Tuple,
    root_certificates: Optional[bytes] = None,
) -> Iterator[Tuple[Callable[[], ServerMessage], Callable[[ClientMessage], None]]]:
    # Possible options:
    # https://github.com/grpc/grpc/blob/v1.43.x/include/grpc/impl/codegen/grpc_types.h
    channel_options = [
        ("grpc.max_send_message_length", GRPC_MAX_MESSAGE_LENGTH),
        ("grpc.max_receive_message_length", GRPC_MAX_MESSAGE_LENGTH),
    ]

    if root_certificates is not None:
        ssl_channel_credentials = grpc.ssl_channel_credentials(root_certificates)
        channel = grpc.secure_channel(
            parent_address, ssl_channel_credentials, options=channel_options
        )
        log(INFO, "Opened secure gRPC connection using certificates")
    else:
        channel = grpc.insecure_channel(parent_address, options=channel_options)
        log(INFO, "Opened insecure gRPC connection (no certificates were passed)")

    channel.subscribe(on_channel_state_change)
    
    stub = FlowerServiceStub(channel)
    queue: Queue[ClientMessage] = Queue(maxsize=1)
    time_iterator = TimeoutIterator(iterator=iter(queue.get, None), reset_on_next=True)

    server_message_iterator: Iterator[ServerMessage] = stub.Join(time_iterator, metadata=metadata)
    timeout_iterator = TimeoutIterator(iterator=server_message_iterator, reset_on_next=True)

    def receive_fn(timeout: Optional[int] = None) -> Tuple[ServerMessage, bool]:
        if timeout is not None:
            timeout_iterator.set_timeout(float(timeout))
        server_message = next(timeout_iterator)
        if server_message is timeout_iterator.get_sentinel():
            return server_message, False
        return server_message, True
    receive: Callable[[Optional[int]], Tuple[ServerMessage, bool]] = receive_fn
    send: Callable[[ClientMessage], None] = lambda msg: queue.put(msg, block=False)

    try:
        yield send, receive
    finally:
        # Release Iterator to avoid leaking memory
        time_iterator.interrupt()
        send(sentinel)
        # Make sure to have a final
        channel.close()
        log(DEBUG, "gRPC channel closed")