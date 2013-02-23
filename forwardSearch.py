#!/usr/bin/env python3

class State(object):
    """This class models the state of the puzlleboard.

    0 encodes the empty tile. Currently only a 3x3 board
    is supported
    """
    def __init__(self):
        pass
        

def forwardSearch(initialstate, goalstate):
    """Implementation for forward search in state space

    This function searches a path from a given initial state
    to the given goal state. It returns the path found.
    """
    print("fwrdsrch called")


# only call if script is executed (and not included)
if __name__ == '__main__':
    goalstate = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    initalstate = [1, 6, 4, 8, 7, 0, 3, 2, 5]
    forwardSearch(initalstate,goalstate)
    print("huha")
