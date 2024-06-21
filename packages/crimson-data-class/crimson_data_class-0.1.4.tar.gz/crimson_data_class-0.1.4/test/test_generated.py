import pytest
from pydantic import BaseModel
from crimson.data_class import DataClassList
from typing import List


class UnitData(BaseModel):
    arg1: int
    arg2: str


class ManyData(DataClassList[UnitData]):
    data: List[UnitData]


@pytest.fixture
def unit_data_list():
    return [UnitData(arg1=i, arg2=f"number {i}") for i in range(10)]


@pytest.fixture
def many_data(unit_data_list):
    return ManyData(data=unit_data_list)


def test_initialization(many_data):
    assert len(many_data.data) == 10
    assert many_data.default_key == "arg1"


def test_get_list_dict(many_data):
    list_dict = many_data.get_list_dict()
    assert len(list_dict) == 10
    assert list_dict[0] == {"arg1": 0, "arg2": "number 0"}


def test_get_dataframe(many_data):
    df = many_data.get_dataframe()
    assert df.shape == (10, 2)
    assert list(df.columns) == ["arg1", "arg2"]


def test_dict_property(many_data):
    data_dict = many_data.dict
    assert len(data_dict) == 10
    assert 0 in data_dict
    assert data_dict[0].arg2 == "number 0"


def test_get_custom_dict(many_data):
    custom_dict = many_data.get_custom_dict("arg2")
    assert len(custom_dict) == 10
    assert "number 0" in custom_dict
    assert custom_dict["number 0"].arg1 == 0


def test_invalid_custom_dict_key(many_data):
    with pytest.raises(AttributeError):
        many_data.get_custom_dict("invalid_key")
