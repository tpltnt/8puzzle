# tests for all actions

import sys
sys.path.append('../8puzzle')
import pytest
from forwardSearch import *


def test_moveLeft():
    centercenter = [1,2,3,4,0,5,6,7,8]
    centerleft = [1,2,3,0,4,5,6,7,8]
    assert centerleft == moveLeft(centercenter)

def test_moveRight():
    centercenter = [1,2,3,4,0,5,6,7,8]
    centerright = [1,2,3,4,5,0,6,7,8]
    assert centerright == moveRight(centercenter)

def test_moveUp():
    centercenter = [1,2,3,4,0,5,6,7,8]
    centertop = [1,0,3,4,2,5,6,7,8]
    assert centertop == moveUp(centercenter)

def test_moveDown():
    centercenter = [1,2,3,4,0,5,6,7,8]
    centerbottom = [1,2,3,4,7,5,6,0,8]
    assert centerbottom == moveDown(centercenter)
