# tests for all actions

import sys
sys.path.append('../8puzzle')
import pytest
from forwardSearch import *


def test_moveLeft():
    centercenter = State([1,2,3,4,0,5,6,7,8])
    centerleft = State([1,2,3,0,4,5,6,7,8])
    assert centerleft == moveLeft(centercenter)

def test_moveLeft_impossible():
    centerleft = State([1,2,3,0,4,5,6,7,8])
    with pytest.raises(RuntimeError):
        moveLeft(centerleft)

def test_moveRight():
    centercenter = State([1,2,3,4,0,5,6,7,8])
    centerright = State([1,2,3,4,5,0,6,7,8])
    assert centerright == moveRight(centercenter)

def test_moveRight_impossible():
    centerright = State([1,2,3,4,5,0,6,7,8])
    with pytest.raises(RuntimeError):
        moveRight(centerright)

def test_moveUp():
    centercenter = State([1,2,3,4,0,5,6,7,8])
    centertop = State([1,0,3,4,2,5,6,7,8])
    assert centertop == moveUp(centercenter)

def test_moveUp_impossible():
    centertop = State([1,0,3,4,2,5,6,7,8])
    with pytest.raises(RuntimeError):
        moveUp(centertop)

def test_moveDown():
    centercenter = State([1,2,3,4,0,5,6,7,8])
    centerbottom = State([1,2,3,4,7,5,6,0,8])
    assert centerbottom == moveDown(centercenter)

def test_moveDown_impossible():
    centerbottom = State([1,2,3,4,7,5,6,0,8])
    with pytest.raises(RuntimeError):
        moveDown(centerbottom)
