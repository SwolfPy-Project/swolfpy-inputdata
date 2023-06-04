import numpy as np
from stats_arrays import MCRandomNumberGenerator, UncertaintyBase


class MC:
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

    def __init__(self, input_dict, process_name):
        """
        Initialize ``MC`` class.
        """
        self.input_dict = input_dict
        self.process_name = process_name

    def setup_MC(self, seed=None):
        """
        Creates `MCRandomNumberGenerator` and store it in ``MC.rand`` attribute.

        :param seed: seed for random number generation
        :type seed: int, optional
        """
        self.list_var = []
        self.sens_analysis = {}
        self.run_index = 0
        self.max_run = 10000000
        k = 0
        for x in self.input_dict.values():
            for y in x:
                self.list_var.append(x[y])
                if "list" in x[y].keys():
                    self.sens_analysis[k] = x[y]["list"]
                    self.max_run = min(self.max_run, len(x[y]["list"]))
                k += 1
        self.Vars = UncertaintyBase.from_dicts(*self.list_var)
        self.rand = MCRandomNumberGenerator(self.Vars, seed=seed)

    def gen_MC(self):
        """
        Generate random numbers and update data. It also returns a list of tuples include
        the name of parameter and generted number.

        :return: List of tuples include the name of parameter and generted number: ``[((parameter_category,parameter),generated_number)]``
        :rtype: list
        """
        data = self.rand.next()
        if len(self.sens_analysis) > 0:
            for x in self.sens_analysis.keys():
                data[x] = self.sens_analysis[x][self.run_index]
            self.run_index += 1
            if self.run_index > self.max_run:
                raise ValueError("Number of runs are more than the number of defined inputs")
        i = 0
        variables = []
        for x in self.input_dict.keys():
            for y in self.input_dict[x]:
                if not np.isnan(data[i]):
                    self.input_dict[x][y]["amount"] = data[i]
                    variables.append(((self.process_name, x, y), data[i]))
                i += 1
        return variables
