# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:25:05 2019

@author: msardar2
"""
from .InputData import InputData
from .CommonData import CommonData
from pathlib import Path


class WTE_Input(InputData):
    def __init__(self, input_data_path=None, process_data_path=None,
                 process_name='WTE', CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / 'Data/WTE_Input.csv'
        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()

        if process_data_path is None:
            process_data_path = Path(__file__).parent / "Data/WTE_Input_MaterialDependent.csv"
        self.add_process_data(process_data_path=process_data_path,
                              index=CommonDataObjct.Index)
