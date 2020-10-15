# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:49:46 2019

@author: msardar2
"""
from stats_arrays import MCRandomNumberGenerator, UncertaintyBase
import numpy as np


class MC():
    """
    .. _Class_MC:

    This class generates random number for Monte-Carlo simulations. This class is the interface to
    `stats_arrays <https://pypi.org/project/stats-arrays/>`_ package.

    The example below is showing the usage of ``stats_arrays``.

    :Example:

    >>> from stats_arrays import *
    >>> my_variables = UncertaintyBase.from_dicts(
    ...     {'loc': 2, 'scale': 0.5, 'uncertainty_type': NormalUncertainty.id},
    ...     {'loc': 1.5, 'minimum': 0, 'maximum': 10, 'uncertainty_type': TriangularUncertainty.id}
    ... )
    >>> my_variables
    array([(2.0, 0.5, nan, nan, nan, False, 3),
           (1.5, nan, nan, 0.0, 10.0, False, 5)],
        dtype=[('loc', '<f8'), ('scale', '<f8'), ('shape', '<f8'),
               ('minimum', '<f8'), ('maximum', '<f8'), ('negative', '?'),
               ('uncertainty_type', 'u1')])
    >>> my_rng = MCRandomNumberGenerator(my_variables)
    >>> my_rng.next()
    array([ 2.74414022,  3.54748507])


    :param input_dict: list of dictionaries that include input data (see the example)
    :type input_dict: list

    >>> from swolfpy_inputdata import MC
    >>> input_dict={'Cat1': {'Par1': {'Name': 'Name1','amount': 1.0,'unit': 'Unit1',
    ...                                 'uncertainty_type': 3,'loc': 1,'scale':0.2 ,'shape': None,
    ...                                 'minimum': None,'maximum': None,
    ...                                 'Reference': None,'Comment': None},
    ...                     'Par2': {'Name': 'Name2','amount': 1.5,'unit': 'Unit2',
    ...                                 'uncertainty_type': 3,'loc': 1.5,'scale': 0.4,'shape': None,
    ...                                 'minimum': None,'maximum': None,
    ...                                 'Reference': None,'Comment': None}}}
    >>> test_MC = MC(input_dict)
    >>> test_MC.setup_MC()
    >>> test_MC.gen_MC()
    [(('Cat1', 'Par1'), 1.0554408376879747),
     (('Cat1', 'Par2'), 1.9366617123732333)]

    """
    def __init__(self, input_dict):
        """ Initialize ``MC`` class
        """
        self.input_dict = input_dict

    def setup_MC(self, seed=None):
        """ Creates `MCRandomNumberGenerator` and store it in ``MC.rand`` attribute

        :param seed: seed for random number generation
        :type seed: int, optional
        """
        self.list_var = list()
        self.sens_analysis = {}
        self.run_index = 0
        self.max_run = 10000000
        k = 0
        for x in self.input_dict.values():
            for y in x:
                self.list_var.append(x[y])
                if 'list' in x[y].keys():
                    self.sens_analysis[k] = x[y]['list']
                    self.max_run = min(self.max_run, len(x[y]['list']))
                k += 1
        self.Vars = UncertaintyBase.from_dicts(*self.list_var)
        self.rand = MCRandomNumberGenerator(self.Vars, seed=seed)

    def gen_MC(self):
        """Generate random numbers and update data. It also returns a list of tuples include the name of parameter and generted number.

        :return: List of tuples include the name of parameter and generted number: ``[((parameter_category,parameter),generated_number)]``
        :rtype: list
        """
        data = self.rand.next()
        if len(self.sens_analysis) > 0:
            for x in self.sens_analysis.keys():
                data[x] = self.sens_analysis[x][self.run_index]
            self.run_index += 1
            if self.run_index > self.max_run:
                raise ValueError('Number of runs are more than the number of defined inputs')
        i = 0
        variables = []
        for x in self.input_dict.keys():
            for y in self.input_dict[x]:
                if not np.isnan(data[i]):
                    self.input_dict[x][y]['amount'] = data[i]
                    variables.append(((x, y), data[i]))
                i += 1
        return(variables)

# =============================================================================
#     def create_uncertainty_from_inputs(self,sheet_name,process_data,seed=None):
#         """Creates `MCRandomNumberGenerator` based on the data related to materials.
#         """
#         self.process_data=process_data
#         self.process_data_1=pd.read_excel(Path(__file__).parent/'Data/Material properties - process modles.xlsx', sheet_name = sheet_name,
#                                           index_col = 'Parameter')
#         self.uncertain_dict = dict()
#         cols = list(self.process_data_1)
#         for col in range(0,len(cols),7):
#             self.uncertain_dict[cols[col]] = list()
#             for val in range(len(self.process_data[cols[col]][3:])):
#                 self.uncertain_dict[cols[col]].append(dict())
#                 if not np.isnan(self.process_data_1[cols[col+1]][3+val]):
#                     self.uncertain_dict[cols[col]][val]['uncertainty_type'] = int(self.process_data_1[cols[col+1]][3+val])
#                     self.uncertain_dict[cols[col]][val]['loc'] = self.process_data_1[cols[col+2]][3+val]
#                     self.uncertain_dict[cols[col]][val]['scale'] = self.process_data_1[cols[col+3]][3+val]
#                     self.uncertain_dict[cols[col]][val]['shape'] = self.process_data_1[cols[col+4]][3+val]
#                     self.uncertain_dict[cols[col]][val]['minimum'] = self.process_data_1[cols[col+5]][3+val]
#                     self.uncertain_dict[cols[col]][val]['maximum'] = self.process_data_1[cols[col+6]][3+val]
#                 else:
#                     self.uncertain_dict[cols[col]][val]['uncertainty_type'] = 1
#
#         self.variables = dict()
#         self.rng = dict()
#         for key in self.uncertain_dict.keys():
#             self.variables[key] = UncertaintyBase.from_dicts(*self.uncertain_dict[key])
#             self.rng[key] = MCRandomNumberGenerator(self.variables[key],seed=seed)
#
#     def uncertainty_input_next(self):
#         """Generate random numbers and update the `process_data`
#         """
#         data = dict()
#         variables = list()
#         for key in self.rng.keys():
#             data[key] = self.rng[key].next()
#             for val in range(len(self.process_data[key][3:])):
#                 if not np.isnan(data[key][val]):
#                     self.process_data.at[(self.process_data_1.index.values[3+val]),key] = data[key][val]
#                     variables.append(((key,self.process_data_1.index.values[3+val]),data[key][val]))
#         return variables
# =============================================================================
