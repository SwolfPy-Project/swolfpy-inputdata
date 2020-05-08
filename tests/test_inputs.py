# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:12:49 2020

@author: msmsa
"""
from swolfpy_inputdata import *

def test_all_inputs():
    A = LF_Input()
    A.setup_MC()
    assert isinstance(A.gen_MC(),list)
    
    assert WTE_Input()
    
    assert Comp_Input()
    
    assert AD_Input()
    
    assert SS_MRF_Input()
    
    assert Reproc_Input()
    
    assert SF_Col_Input()
    
    assert Technosphere_Input()
    
    assert CommonData()
