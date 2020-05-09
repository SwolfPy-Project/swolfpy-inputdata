# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:16:05 2019

@author: msardar2
"""
from pathlib import Path
import pandas as pd

class Technosphere_Input():
    def __init__(self,LCI_path=None,LCI_Reference_path=None,Ecospold2_Path=None):
            
        #Checking the path for technosphere LCI data and writing the technophere database
        if LCI_path:
            self.technosphere_path = LCI_path
        else:
            self.technosphere_path = str(Path(__file__).parent)+'\Data\Technosphere_LCI.csv'
        
        #Checking the path for technosphere LCI references
        if LCI_Reference_path:
            self.LCI_Reference_path = LCI_Reference_path
        else:
            self.LCI_Reference_path = str(Path(__file__).parent)+'\Data\Technosphere_References.csv'
        
        #Checking the path for Ecospold2
        if Ecospold2_Path:
            self.Ecospold2_Path = Ecospold2_Path
        else:
            self.Ecospold2_Path = str(Path(__file__).parent)+'\Data\Ecospold2'
        
        #Read the data
        self.LCI_swolfpy_data = pd.read_csv(self.technosphere_path)
        self.LCI_reference = pd.read_csv(self.LCI_Reference_path,index_col='swolfpy_technosphere_name')
        
        if self.LCI_reference['Reference_activity_id'].count()>0 and self.Ecospold2_Path==None:
            raise ValueError('User should select the path to ecospold files, because of keys in Technosphere_References.csv')