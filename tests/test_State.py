import sys
sys.path.append('../8puzzle')
from forwardSearch import State

def test_isEmpty():
    teststate = State()
    assert True == teststate.isEmpty()
