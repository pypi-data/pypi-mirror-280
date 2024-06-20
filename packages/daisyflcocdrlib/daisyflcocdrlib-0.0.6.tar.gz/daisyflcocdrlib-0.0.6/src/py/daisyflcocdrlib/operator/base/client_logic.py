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
from typing import List, Optional
from threading import Lock
from daisyflcocdrlib.common import (
    FitIns,
    FitRes,
    EvaluateIns,
    EvaluateRes,
    ModelSyncMessage,
)

class ClientLogic():
    """Wrapper which adds SecAgg methods."""
    
    def __init__(self, client) -> None:
        self.client = client
        self.model_buf: Optional[ModelSyncMessage] = None
        self.lock: Lock = Lock()
    
    def set_connector(self, connector):
        self._connector = connector
    
    def set_address(self, server_address):
        self._server_address = server_address
    
    def c2c_model_sync(self, msm: ModelSyncMessage):
        """Called by operator manager."""
        self.model_buf = msm

    def reservation(self,) -> bool:
        if self.lock.locked():
            return False
        self.lock.acquire()
        return True

    def unlock(self,):
        if self.lock.locked():
            self.lock.release()
    
    def disconnect(self):
        pass
    
    def fit(
        self, ins: FitIns,
    ) -> FitRes:
        return self.client.fit(ins)

    def evaluate(
        self, ins: EvaluateIns,
    ) -> EvaluateRes:
        return self.client.evaluate(ins)
