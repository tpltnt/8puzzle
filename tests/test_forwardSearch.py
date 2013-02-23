# tests behavior of forward search

import sys
sys.path.append('../8puzzle')
import pytest
from forwardSearch import *


def test_forwardSearch_correct_call():
    foo = State([1,2,3,4,7,5,6,0,8])
    bar = State([1,2,3,4,7,5,6,8,0])
    # returned plan should be just a moveLeft
    forwardSearch(foo,bar)

def test_forwardSearch_same_state():
    centerbottom = State([1,2,3,4,7,5,6,0,8])
    assert [] == forwardSearch(centerbottom,centerbottom)
