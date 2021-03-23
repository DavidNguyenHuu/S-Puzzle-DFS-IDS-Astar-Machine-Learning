import time
from typing import Tuple

class Node:
    def __int__(self, state, parent, operation, depth, cost):
        self.state = state  # should consist of a list or tuple to represent the state we are currently in
        self.parent = parent  # the other parameters are to keep find the path and the depth and the cost
        self.operation = operation
        self.depth = depth
        self.cost = cost


def create_node(state, parent, operation, depth, cost):
    node1 = Node(state, parent, operation, depth, cost)
    return node1


def move_up(state, index):  # we will pass the state along with the index of the number that we want to move up
    new_state = state  # we will copy the current state then we will swap
    if index not in [0, 1, 2]:  # if the index is not in the upper part of the puzzle then swap with the upper index
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state  # after we swap we return a new state with a new order of numbers
    else:
        return None


def move_down(state, index):  # the other moving functions will work in the same way
    new_state = state
    if index not in [6, 7, 8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_left(state, index):
    new_state = state
    if index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_right(state, index):
    new_state = state
    if index not in [2, 5, 8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def search_node(Node, index):  # search the node by applying all the moves and add the child states to a list
    child_nodes = [create_node(move_right(Node.state, index), Node, "move right", Node.depth + 1, 0),
                   create_node(move_down(Node.state, index), Node, "move down", Node.depth + 1, 0),
                   create_node(move_up(Node.state, index), Node, "move up", Node.depth + 1, 0),
                   create_node(move_left(Node.state, index), Node, "move right", Node.depth + 1, 0)]
    for Node in child_nodes:
        if Node.state is None:  # filtering nodes that have wrong states
            child_nodes.remove(Node)
    return child_nodes  # return a list of child nodes which we will search next if we didn't reach the goal state


def DFS(start, goal, search_path, start_timer):
    nodes_list = [start]  # we will add the first state node to our nodes list
    solution_path = []  # we will use this list to backtrack the solution path
    search_path.append(start.state)  # we will add the node to the search path
    while len(nodes_list) != 0:  # quit if we don't have any nodes left to search
        if start_timer == start_timer + 60:  # quit when timeout
            return "no solution"
        else:
            if start.state == goal:  # we will check if the start node contain the goal
                solution_path.append(start.state)  # we will add the node that contain the goal state first
                while start.parent is not None:  # when we reach the original start node we will stop
                    solution_path.append(start.parent.state)  # we will add the parent node to the path
                start = start.parent  # we will add the parent of the parent node
                return solution_path, search_path  # we will return the solution path with the search path
            else:
                nodes_list.remove(start)  # we will remove the node that we just checked
                for index in start.state:  # for each index in the state of the current node we will apply the search
                    child_list = search_node(start, start.state.index(index))  # we will add the results to a new list
                    for node in nodes_list:  # we will search each node in the child list
                        search_path.append(node)
                        DFS(node.state, goal, start_timer)



# This function performs depth limited search
def DLS(start, goal, max_depth):  # we will pass start node, goal node and maximum depth
    if start == goal:
        return True

    elif max_depth <= 0:  # if the maximum depth is reached then it stops searching.
        return False


# This function performs iterative-deepening Search
def IDS(start, goal, search_path, max_depth):  # we will pass start node, goal node, search path and max depth
    # it will loop through and does iterative deepening search till the maximum depth.
    for limit in range(max_depth):
        if DLS(start, goal, search_path, limit):
            return True
        else:
            False
            
def main():
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    initial_state = [6, 1, 2, 7, 8, 3, 5, 4, 9]
    start = create_node(initial_state, None, None, 0, 0)
    solution = []
    search = []
    timer = time.time()
    solution, search = DFS(start, goal_state, search, timer)


if __name__ == '__main__':
    main()
            
