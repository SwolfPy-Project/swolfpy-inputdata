# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:52:32 2019

@author: msmsa
"""
from .InputData import InputData
from pathlib import Path
import pandas as pd


class SF_Col_Input(InputData):
    def __init__(self,input_data_path = None):
        if input_data_path:
            self.input_data_path = input_data_path
        else:
            self.input_data_path = Path(__file__).parent/'Data/SF_collection_Input.csv'
        
        # Initialize the superclass 
        super().__init__(self.input_data_path)
        
        ### Read Material properties related to the process        
        self.process_data = pd.read_csv(Path(__file__).parent/'Data/SF_collection_Input-Material_dependent.csv',index_col = 'Materials')
        self.process_data.fillna(0,inplace=True)

        ### Read input data        
        self.col=pd.read_csv(Path(__file__).parent/'Data/SF_input_col.csv',index_col='Name',usecols=['Name','RWC','SSR','DSR','MSR','LV','SSYW','SSO','DryRes','REC','WetRes','MRDO','SSYWDO','MSRDO'])
        self.col = self.col.transpose()