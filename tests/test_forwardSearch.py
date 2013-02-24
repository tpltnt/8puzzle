# tests behavior of forward search

import sys
sys.path.append('../8puzzle')
import pytest
from forwardSearch import *


def test_forwardSearch_correct_call():
    foo = State([1,2,3,4,7,5,6,0,8])
    bar = State([1,2,3,4,7,5,6,8,0])
    # returned plan should be just a moveLeft
    assert {0: moveLeft} == forwardSearch(foo,bar)

def test_forwardSearch_same_state():
    centerbottom = State([1,2,3,4,7,5,6,0,8])
    assert {} == forwardSearch(centerbottom,centerbottom)

def test_forwardSearch_first_type_wrong():
    with pytest.raises(TypeError):
        forwardSearch(23,State())

def test_forwardSearch_second_type_wrong():
    with pytest.raises(TypeError):
        forwardSearch(State(),23)

def test_forwardSearch_both_type_wrong():
    with pytest.raises(TypeError):
        forwardSearch(23,42)

def test_getApplicableActions_0():
    expected = {0: moveRight, 1: moveDown}
    topleft = State([0,1,2,3,4,5,6,7,8])
    found = topleft.getApplicableActions()
    assert 2 == len(found)
    assert expected == found

def test_getApplicableActions_5():
    expected = {0: moveUp, 1: moveRight, 2: moveDown, 3: moveLeft}
    centercenter = State([1,2,3,4,0,5,6,7,8])
    found = centercenter.getApplicableActions()
    assert 4 == len(found)
    assert expected == found

def test_getTaxicabMetric_0():
    assert 0 == getTaxicabMetric(0,0)

def test_getTaxicabMetric_09():
    assert 4 == getTaxicabMetric(0,9)

def test_getTaxicabMetric_49():
    assert 2 == getTaxicabMetric(4,9)

def test_getTaxicabMetric_45():
    assert 1 == getTaxicabMetric(4,5)

def test_getTaxicabMetric_47():
    assert 1 == getTaxicabMetric(4,7)

def test_getTaxicabMetric_74():
    assert 1 == getTaxicabMetric(7,4)

def test_getTaxicabMetric_54():
    assert 1 == getTaxicabMetric(5,4)
