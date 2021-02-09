# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:16:05 2019

@author: msardar2
"""
from .InputData import InputData
from .CommonData import CommonData
from pathlib import Path
import pandas as pd


class AD_Input(InputData):
    def __init__(self, input_data_path=None, process_name='AD', CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / 'Data/AD_Input.csv'
        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()

        self.process_data = pd.read_csv(Path(__file__).parent / "Data/AD_Input_MaterialDependent.csv",
                                        index_col=0,
                                        header=0,
                                        skiprows=[1, 2, 3]).loc[CommonDataObjct.Index].astype(float)
        self.process_data.fillna(0, inplace=True)
        self.process_data_info = pd.read_csv(Path(__file__).parent / "Data/AD_Input_MaterialDependent.csv",
                                             index_col=0,
                                             header=0,
                                             nrows=3)
