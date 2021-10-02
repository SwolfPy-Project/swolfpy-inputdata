# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 12:24:40 2021

@author: msardar2
"""
from .InputData import InputData
from .CommonData import CommonData
from pathlib import Path


class GC_Input(InputData):
    def __init__(self, input_data_path=None, process_data_path=None,
                 process_name='GC', CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / 'Data/GC_Input.csv'
        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()

        if process_data_path is None:
            process_data_path = Path(__file__).parent / "Data/GC_Input_MaterialDependent.csv"
        self.add_process_data(process_data_path=process_data_path,
                              index=CommonDataObjct.Index)
