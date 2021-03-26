.. General

======================================================================
Input data for swolfpy's life-cycle process models (swolfpy_inputdata)
======================================================================

.. image:: https://img.shields.io/pypi/v/swolfpy_inputdata.svg
        :target: https://pypi.python.org/pypi/swolfpy_inputdata
        
.. image:: https://img.shields.io/pypi/pyversions/swolfpy_inputdata.svg
    :target: https://pypi.org/project/swolfpy_inputdata/
    :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/swolfpy_inputdata.svg
    :target: https://pypi.org/project/swolfpy_inputdata/
    :alt: License

.. image:: https://img.shields.io/pypi/format/swolfpy_inputdata.svg
    :target: https://pypi.org/project/swolfpy_inputdata/
    :alt: Format

.. image:: https://readthedocs.org/projects/swolfpy/badge/?version=latest
        :target: https://swolfpy.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


* Free software: GNU GENERAL PUBLIC LICENSE V2
* Documentation: https://swolfpy.readthedocs.io.
* Repository: https://bitbucket.org/msm_sardar/swolfpy-inputdata
* Other links: 

  * https://go.ncsu.edu/swolfpy
  * https://jwlevis.wixsite.com/swolf

|
Features
--------
* Input data for Life-cycle process models of swolfpy

  * Common data (e.g., molecular weights, heating values) 
  * Material properties (46 common waste fractions; e.g., Food waste, Yard waste)
  
    * Chemical properties (e.g., carbon content, methane yield)
    * Physical properties (e.g., moisture content, density) 
  * Material dependent process model inputs (e.g., separation efficiency for each waste fraction in the trommel) 
  * Material indepent process model inputs
  
* Built-in Monte Carlo simulation


.. list-table:: Description of columns in the csv file for input data
   :widths: auto
   :header-rows: 1

   * - Field 
     - Description
   * - Category
     - Category of the input (e.g., energy recovery, post closure)
   * - Dictonary_Name
     - Name of the dictionary and attribute (whitespace is not allowed)
   * - Parameter Name
     - Short name of the parameter (whitespace is not allowed)
   * - Parameter Description
     - Longer description of the parameter
   * - Amount
     - Default value for the parameter
   * - Unit
     - Unit of the parameter (e.g., MJ/Mg, kW, hours/day)
   * - Uncertainty_type
     - 0: Undefined, 2: Lognormal, 3: normal, 4: Uniform, 5: Triangular, 7: Discrete Uniform
   * - Loc
     - Mean for lognormal and normal distribution
   * - scale
     - Standard deviation for lognormal and normal distribution
   * - shape
     - Shape parameter for Weibull, Gamma or Beta distributions     
   * - Minimum
     - Lower bound/minimum for lognormal, normal, uniform, triangular, and discrete uniform distributions
   * - maximum
     - Upper bound/maximum for lognormal, normal, uniform, triangular, and discrete uniform distributions
   * - Reference
     - 
   * - Comment
     -
     
|
.. Installation

Installation
------------
1- Download and install miniconda from:  https://docs.conda.io/en/latest/miniconda.html

2- Update conda in a terminal window or anaconda prompt::

        conda update conda

3- Create a new environment for swolfpy::

        conda create --name swolfpy python=3.7

4- Activate the environment::

        conda activate swolfpy

5- Install swolfpy_inputdata in the environment::

        pip install swolfpy_inputdata

6- Use in python (e.g., Landfill model)::

        import swolfpy_inputdata as spid 
        data = spid.LF_Input()
        model.calc()
        #Example: Returs the actk parameter in landfill
        data.LF_gas['actk']
        #Example: Returns input data in dataframe format
        data.Data

.. endInstallation
