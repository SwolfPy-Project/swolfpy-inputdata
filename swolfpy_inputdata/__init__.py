# -*- coding: utf-8 -*-
"""
@author: Mojtaba Sardarmehni

Input data for the swolfpy's life_cycle process models
"""
from .MC import MC
from .InputData import InputData
from .CommonData import CommonData
from .Technosphere_Input import Technosphere_Input
from .LF_Input import LF_Input
from .WTE_Input import WTE_Input
from .Comp_Input import Comp_Input
from .AD_Input import AD_Input
from .SS_MRF_Input import SS_MRF_Input
from .Reproc_Input import Reproc_Input
from .SF_Col_Input import SF_Col_Input
from .TS_Input import TS_Input

__all__ = [
    'MC',
    'InputData',
    'CommonData',
    'Technosphere_Input',
    'LF_Input',
    'WTE_Input',
    'Comp_Input',
    'AD_Input',
    'SS_MRF_Input',
    'Reproc_Input',
    'SF_Col_Input',
    'TS_Input'
]

__version__ = '0.1.7'
