import time
from typing import Tuple


class node:
    def _int_(self, state, parent, operation, depth, cost):
        self.state = state    # should consist of a list or tuple to represent the state we are currently in
        self.parent = parent  # the other parameters are to keep find the path and the depth and the cost
        self.operation = operation
        self.depth = depth
        self.cost = cost


def create_node(state, parent, operation, depth, cost):
    return node(state, parent, operation, depth, cost)


def move_up(state, number_index):   # we will pass the state along with the index of the number that we want to move up
    new_state = state  # we will copy the current state then we will swap
    index = new_state.index(number_index)  # the number will indicate the index that we want to swap with it's neighbors
    if index not in [1, 2, 3]:     # if the index is not in the upper part of the puzzle then swap with the upper index
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state    # after we swap we return a new state with a new order of numbers
    else:
        return None


def move_down(state, number_index):   # the other moving functions will work in the same way
    new_state = state
    index = new_state.index(number_index)
    if index not in [7, 8, 9]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_left(state, number_index):
    new_state = state
    index = new_state.index(number_index)
    if index not in [1, 4, 7]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_right(state, number_index):
    new_state = state
    index = new_state.index(number_index)
    if index not in [3, 6, 9]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def search_node(node, number):  # search the node by applying all the moves and add the child states to a list
    child_nodes = [create_node(move_right(node.state, number), node, "move right", node.depth + 1, 0),
                   create_node(move_down(node.state, number), node, "move down", node.depth + 1, 0),
                   create_node(move_up(node.state, number), node, "move up", node.depth + 1, 0),
                   create_node(move_left(node.state, number), node, "move right", node.depth + 1, 0)]
    for node in child_nodes:
        if node.index is None:
            child_nodes.remove(node)
    return child_nodes  # return a list of child nodes which we will search next if we didn't reach the goal state

def DFS(start, goal, search_path):  # in addition to the start node and the goal state we will pass the search path
    nodes_list = [start]  # we will add the first state node to our nodes list
    solution_path = []  # we will use this list to backtrack the solution path
    search_path.append(start)   # we will add the node to the search path
    while len(nodes_list) != 0:  # quit if we don't have any nodes left to search
        start_timer = time.time()  # we will start the timer
        if start_timer == start_timer + 60:  # quit when timeout
            return "no solution"
        else:
            if start.state == goal:  # we will check if the start node contain the goal
                solution_path.append(start)  # we will add the node that contain the goal state first
                while start.parent is not None:  # when we reach the original start node we will stop
                    solution_path.append(start.parent)  # we will add the parent node to the path
                start = start.parent  # we will add the parent of the parent node
                return solution_path, search_path  # we will return the solution path with the cost
            else:
                nodes_list.remove(start)    # we will remove the node that we just checked
                for index in start.state:   # for each index in the state of the current node we will apply the search
                    child_list = search_node(start, index)  # we will add the results to a new list
                    for node in nodes_list:     # we will search each node in the child list 
                        search_path.append(node)
                        DFS(node.state, goal)






