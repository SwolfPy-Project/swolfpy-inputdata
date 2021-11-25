# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:26:54 2019

@author: msardar2
"""
from .InputData import InputData
from .CommonData import CommonData
from pathlib import Path
import pandas as pd
import ast


class LF_Input(InputData):
    def __init__(self, input_data_path=None, process_data_path=None,
                 process_name='LF', CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / 'Data/LF_Input.csv'

        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()

        if process_data_path is None:
            process_data_path = Path(__file__).parent / "Data/LF_Input_MaterialDependent.csv"
        self.add_process_data(process_data_path=process_data_path,
                              index=CommonDataObjct.Index)

        self.gas_emission_factor = pd.read_csv(Path(__file__).parent / 'Data/LF_Gas_emission_factors.csv',
                                               converters={'Biosphere_key': ast.literal_eval})
        self.gas_emission_factor.fillna('', inplace=True)

        self.lcht_Qlty = pd.read_csv(Path(__file__).parent / 'Data/LF_Leachate_Quality.csv',
                                     converters={'Surface_water': ast.literal_eval, 'Ground_water': ast.literal_eval})
        self.lcht_Qlty.fillna(0, inplace=True)

        self.GasColPlan = pd.read_csv(Path(__file__).parent / 'Data/LF_GasColPlan.csv', index_col=0)
