# tests for all state methods

import sys
sys.path.append('../8puzzle')
import pytest
from forwardSearch import *


def test_constructor_empty():
    teststate = State()
    assert [] == teststate._State__internalstate

def test_constructor_state_valid():
    teststate = State([0,1,2,3,4,5,6,7,8])
    assert [0,1,2,3,4,5,6,7,8] == teststate._State__internalstate

def test_constructor_state_too_short():
    with pytest.raises(TypeError):
        foo = State([0,1,2,3,4,5,6,7])

def test_constructor_state_too_long():
    with pytest.raises(TypeError):
        foo = State([0,1,2,3,4,5,6,7,8,9])

def test_isEmpty():
    teststate = State()
    assert True == teststate.isEmpty()

def test_isEmpty_notfalse():
    teststate = State()
    assert False != teststate.isEmpty()

def test_getInternalState():
    teststate = State([0,3,1,5,4,2,8,7,6])
    assert [0,3,1,5,4,2,8,7,6] == teststate.getInternalState()
