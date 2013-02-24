#!/usr/bin/env python3

import random

class State(object):
    """This class models the state of the puzlleboard.

    0 encodes the empty tile. Currently only a 3x3 board
    is supported. A state is empty by default and has to
    be populated.y
    """

    __internalstate = []

    def __init__(self,state_as_list=[]):
        """Allow creation of empty states or with valid values

        Constructor tests only for valid length, nothing more.
        """
        if len(state_as_list) == 0:
            self.__internalstate = state_as_list
        else:
            if len(state_as_list) != 9:
                raise TypeError("given state of from length")
            self.__internalstate = state_as_list

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

    def getApplicableActions(self):
        """Return set of applicable functions

        You can easily execute the actions by iterating
        over the indexes (without actual knowledge of
        the particular action).
        e.g. action[1](teststate) applies the 2nd action to the given state
        """
        applicables = {}

        try:
            moveUp(self)
            applicables.update({len(applicables.keys()): moveUp})
        except RuntimeError:
            pass

        try:
            moveRight(self)
            applicables.update({len(applicables.keys()): moveRight})
        except RuntimeError:
            pass

        try:
            moveDown(self)
            applicables.update({len(applicables.keys()): moveDown})
        except RuntimeError:
            pass

        try:
            moveLeft(self)
            applicables.update({len(applicables.keys()): moveLeft})
        except RuntimeError:
            pass

        return applicables    



def moveLeft(state):
    """move empty tile to the left, return new state"""
    emptytileindex = state.getInternalState().index(0)
    swapindex = emptytileindex - 1
    if swapindex in (-1,2,5):
        raise RuntimeError("current position does not allow moving to the right")
    swapstate = []
    for val in state.getInternalState():
        swapstate.append(val)
    swapstate[emptytileindex] = swapstate[swapindex]
    swapstate[swapindex] = 0
    return State(swapstate)

def moveRight(state):
    """move empty tile to the right, return new state"""
    emptytileindex = state.getInternalState().index(0)
    swapindex = emptytileindex + 1
    if swapindex in (3,6,9):
        raise RuntimeError("current position does not allow moving to the right")
    swapstate = []
    for val in state.getInternalState():
        swapstate.append(val)
    swapstate[emptytileindex] = swapstate[swapindex]
    swapstate[swapindex] = 0
    return State(swapstate)

def moveUp(state):
    """move empty tile up, return new state"""
    emptytileindex = state.getInternalState().index(0)
    swapindex = emptytileindex - 3
    if swapindex < 0:
        raise RuntimeError("current position does not allow moving up")
    swapstate = []
    for val in state.getInternalState():
        swapstate.append(val)
    swapstate[emptytileindex] = swapstate[swapindex]
    swapstate[swapindex] = 0
    return State(swapstate)

def moveDown(state):
    """move empty tile down, return new state"""
    emptytileindex = state.getInternalState().index(0)
    swapindex = emptytileindex + 3
    if swapindex > 8:
        raise RuntimeError("current position does not allow moving down")
    swapstate = []
    for val in state.getInternalState():
        swapstate.append(val)
    swapstate[emptytileindex] = swapstate[swapindex]
    swapstate[swapindex] = 0
    return State(swapstate)

def forwardSearch(initialstate, goalstate):
    """Implementation for forward search in state space

    This function searches a path from a given initial state
    to the given goal state. It returns the path found.
    """

    if not isinstance(initialstate,State):
        raise TypeError("first argument is not of type 'State'")

    if not isinstance(goalstate,State):
        raise TypeError("second argument is not of type 'State'")

    currentstate = initialstate
    plan = {}
    random.seed()

    while True:
        if currentstate == goalstate:
            return plan
        applicable = currentstate.getApplicableActions()
        options = len(applicable)
        if options == 0:
            raise RuntimeError("no applicable actions found")
        act = random.randint(0, options-1)
        plan.update({len(plan.keys()): appicable[act]})
        currentstate = applicable[act](currentstate)

# only call if script is executed (and not included)
if __name__ == '__main__':
    goalstate = State([0, 1, 2, 3, 4, 5, 6, 7, 8])
    initialstate = State([1, 0, 2, 3, 4, 5, 6, 7, 8])
    #initialstate = State([1, 6, 4, 8, 7, 0, 3, 2, 5])
    forwardSearch(initialstate,goalstate)
