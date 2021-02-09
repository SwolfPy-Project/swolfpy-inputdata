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
    def __init__(self, input_data_path=None, process_name='LF', CommonDataObjct=None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent / 'Data/LF_Input.csv'

        # Initialize the superclass
        super().__init__(self.input_data_path, process_name)

        if not CommonDataObjct:
            CommonDataObjct = CommonData()

        self.gas_emission_factor = pd.read_csv(Path(__file__).parent / 'Data/LF_Gas_emission_factors.csv',
                                               converters={'Biosphere_key': ast.literal_eval})
        self.gas_emission_factor.fillna('', inplace=True)

        self.lcht_coef = pd.read_csv(Path(__file__).parent / 'Data/LF_Leachate_Coeff.csv',
                                     converters={'Surface_water': ast.literal_eval, 'Ground_water': ast.literal_eval})
        self.lcht_coef.fillna(0, inplace=True)

        self.lcht_Alloc = pd.read_csv(Path(__file__).parent / 'Data/LF_Leachate_Allocation.csv',
                                      index_col=0).loc[CommonDataObjct.Index]
