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
"""Handle server messages by calling appropriate client methods."""


from typing import Tuple

from daisyflcocdrlib.common import serde, typing
from daisyflcocdrlib.common.typing import Parameters
from daisyflcocdrlib.common import (
    FitRes,
    EvaluateRes,
    Status,
    Code,
    METRICS,
    CURRENT_ROUND,
)
from daisyflcocdrlib.proto.transport_pb2 import ClientMessage, Reason, ServerMessage
from daisyflcocdrlib.utils.task_manager import TaskManager

# pylint: disable=missing-function-docstring


class UnknownServerMessage(Exception):
    """Signifies that the received message is unknown."""


def handle(
    server_msg: ServerMessage,
    task_manager: TaskManager,
) -> ClientMessage:
    """Handle incoming messages from the server.

    Parameters
    ----------
    client : Client
        The Client instance provided by the user.

    Returns
    -------
    client_message: ClientMessage
        The message comming from the server, to be processed by the client.
    sleep_duration : int
        Number of seconds that the client should disconnect from the server.
    keep_going : bool
        Flag that indicates whether the client should continue to process the
        next message from the server (True) or disconnect and optionally
        reconnect later (False).
    """
    field = server_msg.WhichOneof("msg")
    if field == "fit_ins":
        return _fit(server_msg.fit_ins, task_manager)
    if field == "evaluate_ins":
        return _evaluate(server_msg.evaluate_ins, task_manager)
    raise UnknownServerMessage()


def _fit(fit_msg: ServerMessage.FitIns, task_manager: TaskManager) -> ClientMessage:
    # Deserialize fit instruction
    fit_ins = serde.fit_ins_from_proto(fit_msg)
    # Perform fit
    parameters, report =  task_manager.receive_task(parameters=fit_ins.parameters, task_config=fit_ins.config)
   
    if not report.config.__contains__(CURRENT_ROUND):
        report.config[CURRENT_ROUND] = fit_ins.config[CURRENT_ROUND]
    if not report.config.__contains__(METRICS):
        report.config[METRICS] = {}
   
    # Serialize fit result
    fit_res_proto = serde.fit_res_to_proto(FitRes(
        status=Status(code=Code.OK, message="Success"),
        parameters=parameters,
        config=report.config,
    ))
    return ClientMessage(fit_res=fit_res_proto)


def _evaluate(evaluate_msg: ServerMessage.EvaluateIns, task_manager: TaskManager) -> ClientMessage:
    # Deserialize evaluate instruction
    evaluate_ins = serde.evaluate_ins_from_proto(evaluate_msg)
    # Perform evaluation
    _, report =  task_manager.receive_task(parameters=evaluate_ins.parameters , task_config=evaluate_ins.config)

    if not report.config.__contains__(CURRENT_ROUND):
        report.config[CURRENT_ROUND] = evaluate_ins.config[CURRENT_ROUND]
    if not report.config.__contains__(METRICS):
        report.config[METRICS] = {}

    # Serialize evaluate result
    evaluate_res_proto = serde.evaluate_res_to_proto(EvaluateRes(
        status=Status(code=Code.OK, message="Success"),
        config=report.config,
    ))
    return ClientMessage(evaluate_res=evaluate_res_proto)
