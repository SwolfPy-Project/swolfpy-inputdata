# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 11:11:58 2020

@author: msardar2
"""
from .InputData import InputData
from .CommonData import CommonData
from pathlib import Path


class SS_MRF_Input(InputData):
    def __init__(self, input_data_path=None, process_data_path=None,
                 process_name='SS_MRF', CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / 'Data/SS_MRF_Input.csv'

        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()

        if process_data_path is None:
            process_data_path = Path(__file__).parent / "Data/SS_MRF_Input_MaterialDependent.csv"
        self.add_process_data(process_data_path=process_data_path,
                              index=CommonDataObjct.Index)
