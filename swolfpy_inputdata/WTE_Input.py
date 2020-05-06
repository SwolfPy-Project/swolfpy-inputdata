# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 12:25:05 2019

@author: msardar2
"""
from .InputData import InputData
from pathlib import Path
import pandas as pd

class WTE_Input(InputData):
    def __init__(self,input_data_path = None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent/'Data/WTE_Input.csv'
        # Initialize the superclass 
        super().__init__(self.input_data_path)
        
        self.process_data=pd.read_excel(Path(__file__).parent/'Data/Material properties - process modles.xlsx', sheet_name = 'WTE', index_col = 'Parameter')
        self.process_data.fillna(0,inplace=True)