"""
Tests for `swolfpy_inputdata` package.
"""

from copy import deepcopy
from pathlib import Path

import pytest

from swolfpy_inputdata import InputData


@pytest.fixture(scope="module")
def Input_Data():
    A = InputData(Path(__file__).parent / "Test_Input.csv", process_name="test")
    yield A


def test_InputData(Input_Data):
    assert list(Input_Data.Data.columns) == [
        "Category",
        "Dictonary_Name",
        "Parameter Name",
        "Parameter Description",
        "amount",
        "unit",
        "uncertainty_type",
        "loc",
        "scale",
        "shape",
        "minimum",
        "maximum",
        "Reference",
        "Comment",
    ]
    assert Input_Data.Dic1
    assert Input_Data.Dic2
    assert Input_Data.Dic1["Par1"]["Parameter Description"] == "Name1"
    assert Input_Data.Dic1["Par1"]["amount"] == 1
    assert Input_Data.Dic1["Par1"]["uncertainty_type"] == 0


def test_update_InputData(Input_Data):
    newdata = deepcopy(Input_Data.Data)
    # add uncertainty to Par2 of Dic1
    newdata.loc[1, "amount"] = 3
    newdata.loc[1, "uncertainty_type"] = 3
    newdata.loc[1, "loc"] = 3
    newdata.loc[1, "scale"] = 0.5

    Input_Data.Update_input(newdata)
    assert Input_Data.Dic1["Par2"]["uncertainty_type"] == 3
    assert Input_Data.Dic1["Par2"]["amount"] == 3
    assert Input_Data.Dic1["Par2"]["loc"] == 3
    assert Input_Data.Dic1["Par2"]["scale"] == 0.5


def test_setup_MC(Input_Data):
    Input_Data.setup_MC()
    assert Input_Data.Dic1["Par2"]["amount"] == 3
    assert isinstance(Input_Data.gen_MC(), list)
    assert isinstance(Input_Data.gen_MC()[0], tuple)
    assert Input_Data.gen_MC()[0][0] == ("test", "Cat1", "Par2")
    assert abs(Input_Data.gen_MC()[0][1] - 3) <= 2
