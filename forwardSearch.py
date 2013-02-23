#!/usr/bin/env python3

class State(object):
    """This class models the state of the puzlleboard.

    0 encodes the empty tile. Currently only a 3x3 board
    is supported. A state is empty by default and has to
    be populated.y
    """

    __internalstate = []

    def __init__(self,state=[]):
        """Allow creation of empty states or with valid values

        Constructor tests only for valid length, nothing more.
        """
        if len(state) == 0:
            self.__internalstate = state
        else:
            if len(state) != 9:
                raise TypeError("given state of from length")
            self.__internalstate = state

    # equality operator for states
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._State__internalstate == other._State__internalstate
        else:
            return False

    # in-equality operator
    def __ne__(self, other):
        return not self.__eq__(other)

    def isEmpty(self):
        """Test if internal state is emtpy."""
        if [] == self.__internalstate:
            return True
        else:
            return False

    def getInternalState(self):
        """Return internal array of the State"""
        return self.__internalstate

def moveLeft(state):
    """move empty tile to the left, return new state"""
    return state

def moveRight(state):
    """move empty tile to the right, return new state"""
    return state

def moveUp(state):
    """move empty tile up, return new state"""
    return state

def moveDown(state):
    """move empty tile down, return new state"""
    emptytileindex = state.getInternalState().index(0)
    swapindex = emptytileindex + 3
    if swapindex > 8:
        raise RuntimeError("current position does not allow moving down")
    swapstate = state.getInternalState()
    swapstate[emptytileindex] = swapstate[swapindex]
    swapstate[swapindex] = 0
    return State(swapstate)

def forwardSearch(initialstate, goalstate):
    """Implementation for forward search in state space

    This function searches a path from a given initial state
    to the given goal state. It returns the path found.
    """

    currentstate = initialstate
    plan = []


# only call if script is executed (and not included)
if __name__ == '__main__':
    goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    initalstate = [1, 6, 4, 8, 7, 0, 3, 2, 5]
    forwardSearch(initalstate,goalstate)
