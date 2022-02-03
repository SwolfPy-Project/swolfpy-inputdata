# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:12:49 2020

@author: msmsa
"""
import swolfpy_inputdata as si


def test_all_inputs():
    A = si.LF_Input()
    A.setup_MC()
    assert isinstance(A.gen_MC(), list)

    assert si.WTE_Input()

    assert si.Comp_Input()

    assert si.AD_Input()

    assert si.SS_MRF_Input()

    assert si.Reproc_Input()

    assert si.SF_Col_Input()

    assert si.MF_Col_Input()

    assert si.COM_Col_Input()

    assert si.Technosphere_Input()

    assert si.CommonData()

    assert si.GC_Input()

    assert si.RDF_Input()

    assert si.HC_Input()

    assert si.TS_Input()

    assert si.AnF_Input()
