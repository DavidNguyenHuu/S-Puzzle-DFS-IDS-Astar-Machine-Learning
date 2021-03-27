# https://www.annytab.com/a-star-search-algorithm-in-python/
import copy


class Node:
    def __init__(self, state: (), parent: ()):
        self.state = state
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f


def astar_search(start, goal):
    open = []
    closed = []
    search = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(goal, None)

    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        search.append(current_node.state)
        # print(current_node.g)
        # print(current_node.f)
        # Check if we have reached the goal, return the path
        if current_node.state == goal_node.state:
            path = []
            while current_node.state != start_node.state:
                path.append(current_node.state)
                current_node = current_node.parent
            path.append(start)
            print("Solution path for A*: ", path[::-1])
            print("Search path for A*: ", search)
            return path[::-1]

        # Get neighbors
        neighbors = get_neighbors(current_node.state)

        # Loop neighbors
        for next in neighbors:
            # Create a neighbor node
            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if neighbor in closed:
                continue
            # Generate heuristics, g = num of steps from start, h = num of tiles not in goal state
            counth = 0
            for row in range(len(next)):
                for col in range(len(next[row])):
                    if next[row][col] != goal[row][col]:
                        counth += 1;
            neighbor.g = current_node.g + 1
            neighbor.h = counth
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open(open, neighbor):
                open.append(neighbor)
    # Return None, no path is found
    return None


# Get all next possible steps
def get_neighbors(current_state):
    neighbors = []
    for row in range(len(current_state)):
        for col in range(len(current_state[row])):
            # switch up
            if row != 0:
                temp_state = copy.deepcopy(current_state)
                temp_state[row][col] = current_state[row - 1][col]
                temp_state[row - 1][col] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
            # switch down
            if row != len(current_state) - 1:
                temp_state = copy.deepcopy(current_state)
                temp_state[row][col] = current_state[row + 1][col]
                temp_state[row + 1][col] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
            # switch left
            if col != 0:
                temp_state = copy.deepcopy(current_state)
                temp_state[row][col] = current_state[row][col - 1]
                temp_state[row][col - 1] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
            # switch right
            if col != len(current_state) - 1:
                temp_state = copy.deepcopy(current_state)
                temp_state[row][col] = current_state[row][col + 1]
                temp_state[row][col + 1] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
    return neighbors


# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if neighbor.state == node.state and neighbor.f >= node.f:
            return False
    return True

def main():
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    start = [[6, 1, 2], [7, 8, 3], [5, 4, 9]]
    astar_search(start, goal)


if __name__ == "__main__": main()
