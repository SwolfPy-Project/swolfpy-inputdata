# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:45:14 2020

@author: msmsa
"""
import pandas as pd
from .MC import MC
import ast


class InputData(MC):
    """
    ``InputData`` class reads the input data from the csv file and load them as class attributes. This class is inherited from the ``MC`` class.

    Main functionalities include:
    loading data, updating data and generating random number for data based on the defined probabiliy distributions.

    :param input_data_path: absolute path to the input data file
    :type input_data_path: str
    :param eval_parameter: If the parameters are tuple instead of str, it will evalute their real value.
    :type eval_parameter: bool, optional

    """
    def __init__(self, input_data_path, process_name, eval_parameter=False):
        """Initialize ``InputData`` class
        """
        self.input_data_path = input_data_path
        self.process_name = process_name
        self.Data = pd.read_csv(self.input_data_path, dtype={'amount': float, 'uncertainty_type': float, 'loc': float,
                                                             'scale': float, 'shape': float, 'minimum': float, 'maximum': float})

        if eval_parameter:
            self.Data['Parameter Name'] = self.Data['Parameter Name'].apply(ast.literal_eval)

        # Setting uncertainty type to 0 : Undefined ; when it is not defined
        self.Data['uncertainty_type'].fillna(0, inplace=True)
        # self.Data=self.Data.where((pd.notnull(self.Data)), None)
        self.Input_dict = {}
        self.keys = self.Data.columns[3:]
        for i in range(len(self.Data)):
            if self.Data.Category[i] not in self.Input_dict.keys():
                exec("self.%s = {}" % self.Data.Dictonary_Name[i])
                exec("self.Input_dict[self.Data.Category[i]] = self.%s" % self.Data.Dictonary_Name[i])
                exec("self.%s[self.Data['Parameter Name'][i]] = dict(zip(self.keys,self.Data.loc[i,'Parameter Description':]))" %
                     self.Data.Dictonary_Name[i])
            else:
                exec("self.%s[self.Data['Parameter Name'][i]] = dict(zip(self.keys,self.Data.loc[i,'Parameter Description':]))" %
                     self.Data.Dictonary_Name[i])

### Add process data
    def add_process_data(self, process_data_path, index):
        self.process_data = pd.read_csv(process_data_path,
                                        index_col=0,
                                        header=0,
                                        skiprows=[1, 2, 3]).loc[index].astype(float)
        self.process_data.fillna(0, inplace=True)
        self.process_data_info = pd.read_csv(process_data_path,
                                             index_col=0,
                                             header=0,
                                             nrows=3)

### Update_Input
    def Update_input(self, NewData):
        """ Get a new DataFrame and update the ``data`` in ``InputData`` class.

        :param NewData:
        :type NewData: 'pandas.DataFrame'
        """
        for i in NewData.index:
            exec("self.%s[NewData['Parameter Name'][i]] = dict(zip(self.keys,NewData.loc[i,'Parameter Description':]))" % NewData.Dictonary_Name[i])
            self.Data.loc[i] = NewData.loc[i]

### Monte_carlo
    def setup_MC(self, seed=None):
        """ Initialize the parent class (``MC``) and create ``MCRandomNumberGenerator`` based on the data for uncertainty distributions via
        calling ``MC.setupMC()`` method.

        :param seed: seed for random number generation
        :type seed: int, optional

        .. seealso:: Class_MC_
        """
        super().__init__(self.Input_dict, self.process_name)
        super().setup_MC(seed)

### Reset static Values
    def reset_static_vals(self):
        for i in self.Data.index:
            exec("self.%s[self.Data['Parameter Name'][i]]['amount'] = self.Data.loc[i,'amount']" % self.Data.Dictonary_Name[i])
