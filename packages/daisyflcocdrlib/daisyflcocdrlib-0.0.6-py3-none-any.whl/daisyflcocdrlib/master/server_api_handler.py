from flask import Flask, request, make_response, Response , jsonify
from typing import Callable
from daisyflcocdrlib.utils.task_manager import TaskManager
import threading
from daisyflcocdrlib.common import (
    CURRENT_ROUND,
    PARTICIPATION,
    SUBTASK_RETURNS_SELECTED,
    SUBTASK_RETURNS_RESULTS,
    SUBTASK_RETURNS_FAILURES,
    SUBTASK_RETURNS_ROAMING,
    SUBTASK_TIMER,
    TIMER_ROUND,
    METRICS,
    LOSS,
    ACCURACY,
)
import timeit
import csv
import re
from sklearn.metrics import mean_squared_error
import numpy as np
from pathlib import Path
import os
import pandas as pd

class ServerListener:
    def __init__(
            self,
            ip: str,
            port: int,
            task_manager: TaskManager,
        ):
        self.app = Flask(__name__)
        self._ip: str = ip
        self._port: int = port
        self._task_manager: TaskManager = task_manager
        self.data_preprocess()
        self.res = {}
        self._timer = timeit.default_timer() - 10
        self.files = {}

        @self.app.route("/publish_task", methods=["POST"])
        def publish_task():
            js = request.get_json()
            self._task_manager.receive_task(task_config=js)
            return js, 200
        
        @self.app.route("/upload_metrics", methods=["POST"])
        def upload_metrics():
            string_data = request.form.get('string_data')
            file = request.files.get('file')
    
            if not string_data:
                return jsonify({'Error': 'No string data provided'}), 400

            if not file:
                return jsonify({'Error': 'No file provided'}), 400
            
            
            
            df = pd.read_csv(file)
            if self.files.__contains__(string_data):
                if self.files[string_data].equals(df):
                    return jsonify({}), 200

            self.files[string_data] = df
            self.res[string_data]=""
            predict_rmse_dict = {}
            actual_rmse_dict = {}
            type = re.search(r'_(finetuned|pretrained)_', string_data)
            bs_id = re.search(r'bs\d+', string_data).group(0)[2:]

            for colname , col in df.items():
                if colname == "Timestep":
                    timestep = col.tolist()
                    continue
    
                match1 = re.match(r'(\d+)_actuals', colname)
                match2 = re.match(r'(\d+)_predictions', colname)
    
                if match1:
                    pre_ue = match1.group(1)
                    ue_number = self.imsi_to_ue.get(int(pre_ue), "Unknown IMSI")

                    col = col.tolist()
                    col = [float(x) for x in col]
                
                    actual_rmse_dict[ue_number] = col

                    tx_brate_mean = []
                    for i in range(len(timestep)):
                        labels_act = f'{{time="{timestep[i]}",bs="{bs_id}",ue="{ue_number}",slice_id="0",type="actuals"}}'
                        labels_mean = f'{{time="{timestep[i]}",bs="{bs_id}",ue="{ue_number}",slice_id="0",type="actuals mean"}}'                

                        if len(tx_brate_mean) < 10:
                            tx_brate_mean.append(col[i])
                        else :
                            tx_brate_mean.pop(0)
                            tx_brate_mean.append(col[i])

                    
                        self.res[string_data] += "# HELP tx_brate_downlink tx_brate_downlink\n"
                        self.res[string_data] += "# TYPE tx_brate_downlink gauge\n"
                        self.res[string_data] += f'tx_brate_downlink{labels_mean} {sum(tx_brate_mean) / len(tx_brate_mean)}\n'

                        self.res[string_data] += "# HELP tx_brate_downlink tx_brate_downlink\n"
                        self.res[string_data] += "# TYPE tx_brate_downlink gauge\n"
                        self.res[string_data] += f'tx_brate_downlink{labels_act} {f"{col[i]:.10f}"}\n'

                if match2:
                    pre_ue = match2.group(1)
                    ue_number = self.imsi_to_ue.get(int(pre_ue), "Unknown IMSI")

                    col = col.tolist()
                    col = [float(x) for x in col]

                    predict_rmse_dict[ue_number]=col
                    
                    for i in range(len(timestep)):
                        labels_predict = f'{{time="{timestep[i]}",bs="{bs_id}",ue="{ue_number}",slice_id="0",type="{type.group(1)}"}}'

                        self.res[string_data] += "# HELP tx_brate_downlink tx_brate_downlink\n"
                        self.res[string_data] += "# TYPE tx_brate_downlink gauge\n"
                        self.res[string_data] += f'tx_brate_downlink{labels_predict} {f"{col[i]:.10f}"}\n'

            for key in list(predict_rmse_dict.keys()):
                mse = mean_squared_error(predict_rmse_dict[key], actual_rmse_dict[key])
                rmse = np.sqrt(mse)
                
                labels_rmse = f'{{bs="{bs_id}",ue="{key}",slice_id="0",type="{type.group(1)}",rmse_type="{type.group(1)}"}}'
                self.res[string_data] += "# HELP rmse rmse\n"
                self.res[string_data] += "# TYPE rmse gauge\n"
                self.res[string_data] += f'rmse{labels_rmse} {rmse}\n'

            # print(f'File content:\n{df}')
            # df.to_csv(string_data, index=False)
            
            return jsonify({}), 200

        @self.app.route("/metrics")
        def metrics():
            # if timeit.default_timer() - self._timer > 10:
            #    self.read_file()
            #    self._timer = timeit.default_timer()
            #print(list(self.res.keys()))
            s = ""
            for key in list(self.res.keys()):
                s+=self.res[key]
            #print(s)
            response = make_response(s)
            response.headers["content-type"] = "text/plain"
            return response

    def data_preprocess(self,):
        urllc = [1,4,7,10,11,14,17,20,21,24,27,30,31,34,37,40]
        embb_ue = [2,5,8,12,15,18,22,25,28,32,35,38]
        mtc_ue = [3,6,9,13,16,19,23,26,29,33,36,39]

        self.ue_imsi = [1010123456000 + i for i in range(2,45)]
        self.ue_imsi.remove(1010123456012)
        self.ue_imsi.remove(1010123456023)
        self.ue_imsi.remove(1010123456034)

        self.slice = {}
        for ue in urllc:
            self.slice[ue] = 2
        for ue in embb_ue:
            self.slice[ue] = 0
        for ue in mtc_ue:
            self.slice[ue] = 1

        self.imsi_to_ue = {imsi: i+1 for i, imsi in enumerate(self.ue_imsi)}
        return


    def read_file(self,):
        self.res = ""
        predict_rmse_dict = {}
        actual_rmse_dict = {}
        # for bs_path in paths:
        #     if not os.path.isfile(Path(bs_path)):
        #         print(f"Cannot find {bs_path}.")
        #         return

        for fkey in list(self.files.keys()):
            df = self.files[fkey]
            type = re.search(r'_(.*?)_', fkey)
            for colname , col in df.items():

                if colname == "Timestep":
                    timestep = col.tolist()
                    continue
    
                match1 = re.match(r'(\d+)_actuals', colname)
                match2 = re.match(r'(\d+)_predictions', colname)
    
                if match1:
                    pre_ue = match1.group(1)
                    ue_number = self.imsi_to_ue.get(int(pre_ue), "Unknown IMSI")

                    col = col.tolist()
                    col = [float(x) for x in col]
                
                    actual_rmse_dict[ue_number] = col

                    for i in range(len(timestep)):
                        labels_act = f'{{time="{timestep[i]}",bs="{fkey[2]}",ue="{ue_number}",slice_id="0",type="actuals"}}'

                        self.res += "# HELP tx_brate_downlink tx_brate_downlink\n"
                        self.res += "# TYPE tx_brate_downlink gauge\n"
                        self.res += f'tx_brate_downlink{labels_act} {f"{col[i]:.10f}"}\n'

                if match2:
                    pre_ue = match2.group(1)
                    ue_number = self.imsi_to_ue.get(int(pre_ue), "Unknown IMSI")

                    col = col.tolist()
                    col = [float(x) for x in col]

                    predict_rmse_dict[ue_number]=col
                    
                    for i in range(len(timestep)):
                        labels_predict = f'{{time="{timestep[i]}",bs="{fkey[2]}",ue="{ue_number}",slice_id="0",type="{type.group(1)}"}}'

                        self.res += "# HELP tx_brate_downlink tx_brate_downlink\n"
                        self.res += "# TYPE tx_brate_downlink gauge\n"
                        self.res += f'tx_brate_downlink{labels_predict} {f"{col[i]:.10f}"}\n'

            for key in list(predict_rmse_dict.keys()):
                mse = mean_squared_error(predict_rmse_dict[key], actual_rmse_dict[key])
                rmse = np.sqrt(mse)

                labels_rmse = f'{{bs="{fkey[2]}",ue="{key}",slice_id="0",type="{type.group(1)}",rmse_type=""}}'
                self.res += "# HELP rmse rmse\n"
                self.res += "# TYPE rmse gauge\n"
                self.res += f'rmse{labels_rmse} {rmse}\n'

                del predict_rmse_dict[key]
                del actual_rmse_dict[key]
           
        return

    def run(self,):
        self.app.run(host=self._ip, port=self._port)

