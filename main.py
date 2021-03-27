import time
from typing import Tuple

from astar import a_star_search


class Node:
    def __init__(self, state, parent, depth, cost):
        self.state = state  # should consist of a list or tuple to represent the state we are currently in
        self.parent = parent  # the other parameters are to keep find the path and the depth and the cost
        self.depth = depth
        self.cost = cost


def create_node(state, parent, depth, cost):
    node1 = Node(state, parent, depth, cost)
    return node1


def move_up(state, row, column):  # we will pass the state along with the index of the number that we want to move up
    new_state = state  # we will copy the current state then we will swap
    if row != 0:  # if the index is not in the upper part of the puzzle then swap with the upper index
        temp = new_state[row - 1][column]
        new_state[row - 1][column] = new_state[row][column]
        new_state[row][column] = temp
        return new_state  # after we swap we return a new state with a new order of numbers
    else:
        return None


def move_down(state, row, column):  # the other moving functions will work in the same way
    new_state = state
    if row != 2:
        temp = new_state[row + 1][column]
        new_state[row + 1][column] = new_state[row][column]
        new_state[row][column] = temp
        return new_state
    else:
        return None


def move_left(state, row, column):
    new_state = state
    if column != 0:
        temp = new_state[row][column - 1]
        new_state[row][column - 1] = new_state[row][column]
        new_state[row][column] = temp
        return new_state
    else:
        return None


def move_right(state, row, column):
    new_state = state
    if column != 2:
        temp = new_state[row][column + 1]
        new_state[row][column + 1] = new_state[row][column]
        new_state[row][column] = temp
        return new_state
    else:
        return None


def search_node(Node, row, column):  # search the node by applying all the moves and add the child states to a list
    child_nodes = [create_node(move_right(Node.state, row, column), Node, Node.depth + 1, 0),
                   create_node(move_down(Node.state, row, column), Node, Node.depth + 1, 0),
                   create_node(move_up(Node.state, row, column), Node, Node.depth + 1, 0),
                   create_node(move_left(Node.state, row, column), Node, Node.depth + 1, 0)]
    for Node in child_nodes:
        if Node.state is None:  # filtering nodes that have wrong states
            child_nodes.remove(Node)
    return child_nodes  # return a list of child nodes which we will search next if we didn't reach the goal state


def DFS(start, goal):
    nodes_list = []  # we will add the first state node to our nodes list
    search = []
    start_timer = time.time()
    nodes_list.append(start)
    solution_path = []  # we will use this list to backtrack the solution path
    while len(nodes_list) != 0:  # quit if we don't have any nodes left to search
        end_time = time.time()
        if end_time >= start_timer + 60:  # quit when timeout
            print("no solution")
        else:
            test_node = nodes_list.pop(0)  # we will remove the node that we just checked
            search.append(test_node.state)  # we will add the node to the search path
            if test_node.state == goal:  # we will check if the start node contain the goal
                solution_path.append(test_node.state)  # we will add the node that contain the goal state first
                while test_node.parent is not None:  # when we reach the original start node we will stop
                    solution_path.append(test_node.parent.state)  # we will add the parent node to the path
                    test_node = test_node.parent  # we will add the parent of the parent node
                print("the solution path for DFS :", solution_path)
                print("the search path for DFS :", search)
                return search  # we will return the solution path with the search path
            else:
                if test_node.state is not None:
                    for i in range(len(test_node.state)):
                        for j in range(len(test_node.state[i])):
                            child_list = search_node(test_node, i, j)  # we will add the results to a new list
                            for node in child_list:
                                if node.state not in search:
                                    nodes_list.append(node)


# This function performs iterative-deepening Search
def IDS(start, goal, max_depth):  # we will pass start node, goal node, search path and max depth
    # it will loop through and does iterative deepening search till the maximum depth.
    for depth_limit in range(max_depth):
        result= DLS(start, goal, depth_limit)
        if result == goal:
            return result
        else:
            depth_limit += 1
            
 # This function performs depth limited search
def DLS(start, goal, max_depth):  # we will pass start node, goal node and maximum depth
    open_list = []
    search = []
    solution_path = []
    depth_limit = max_depth
    open_list.append(start)

    while len(open_list) != 0:
        test_node = open_list.pop(0)
        new_node = search.append(test_node.state)
        if new_node == goal:
            return solution_path.append(new_node.state)
        else:
            if max_depth < depth_limit:
                new_node.append(open_list.state)           

                
def main():
    goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    initial_state = ((6, 1, 2), (7, 8, 3), (5, 4, 9))
    initial_state2 = ((2, 1, 3), (4, 5, 6), (7, 8, 9))
    goal_state_list = [list(i) for i in goal_state]
    initial_state_list = [list(i) for i in initial_state]
    initial_state_list2 = [list(i) for i in initial_state2]
    start = create_node(initial_state_list2, None, 0, 0)
    DFS(start, goal_state_list)

    # A* Tests, will remove
    # initial_state = ((6, 1, 2), (7, 8, 3), (5, 4, 9))
    # same solution path, inadmissible smaller search path
    # initial_state = ((5, 4, 9), (6, 1, 2), (7, 8, 3))
    # admissible lower cost solution path, inadmissible smaller search path

    # true => use admissible heuristic, if false => use inadmissible heuristic
    a_star_search(initial_state, goal_state, True)
    a_star_search(initial_state, goal_state, False)


if __name__ == '__main__':
    main()
