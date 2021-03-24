# https://www.annytab.com/a-star-search-algorithm-in-python/

# This class represents a node
class Node:
    # Initialize the class
    def __init__(self, position: (), parent: ()):
        self.state = position
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.state == other.state

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return '({0},{1})'.format(self.state, self.f)


# A* search
def astar_search(start, goal):
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(goal, None)
    # Add the start node
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        # Sort the open list to get the node with the lowest cost first
        open.sort()
        # Get the node with the lowest cost
        current_node = open.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.state)
                current_node = current_node.parent
            # path.append(start)
            # Return reversed path
            # return path[::-1]
            return 'done'

        # Get neighbors
        neighbors = get_neighbors(current_node.state)

        # Loop neighbors
        for next in neighbors:
            # Create a neighbor node
            neighbor = Node(next, current_node)
            # Check if the neighbor is in the closed list
            if neighbor in closed:
                continue
            # Generate heuristics
            count = 0
            for row in range(len(next)):
                for col in range(len(next[row])):
                    if next[row][col] == goal[row][col]:
                        count += 1;
            neighbor.g = 0
            neighbor.h = count
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            if add_to_open(open, neighbor):
                # Everything is green, add neighbor to open list
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
                temp_state = current_state
                temp_state[row][col] = current_state[row - 1][col]
                temp_state[row - 1][col] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
            # switch down
            if row != len(current_state) - 1:
                temp_state = current_state
                temp_state[row][col] = current_state[row + 1][col]
                temp_state[row + 1][col] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
            # switch left
            if col != 0:
                temp_state = current_state
                temp_state[row][col] = current_state[row][col - 1]
                temp_state[row][col - 1] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
            # switch right
            if col != len(current_state) - 1:
                temp_state = current_state
                temp_state[row][col] = current_state[row][col + 1]
                temp_state[row][col + 1] = current_state[row][col]
                if temp_state not in neighbors:
                    neighbors.append(temp_state)
    return neighbors


# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if neighbor == node and neighbor.f >= node.f:
            return False
    return True


# The main entry point for this module
def main():
    start = None
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    size = 3

    # Create puzzle WIP
    start = [[6, 1, 2], [7, 8, 3], [5, 4, 9]]

    # Find the closest path from start to goal
    path = astar_search(start, goal)
    print()
    print(path)


if __name__ == "__main__": main()
