#!/usr/bin/env python3

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
