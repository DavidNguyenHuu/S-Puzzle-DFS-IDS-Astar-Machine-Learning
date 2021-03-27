from main import Node, create_node

#logic : do dfs with a depth cutoff, generates solution as it goes on , hence why it does not need much memory.

def main():
 
    goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    initial_state2 = ((2, 1, 3), (4, 5, 6), (7, 8, 9))
    initial_state_list2 = [list(i) for i in initial_state2]
    start = create_node(initial_state_list2, None, 0, 0)  # (state,parent,depth,cost)

    IDS(start, goal_state)



def IDS(initial_state, goal_state):
    
    open = []
    closed = []
    maxDepth = 0
    depth_cutoff = 10
    open.append(initial_state)

    for i in range(depth_cutoff):
        while (len(open) > 0):

            if len(closed) == 0:
                node = open.pop()
                closed.append(node)
            else:
                closed.append(node)
                node = open.pop()

            if (node.state == goal_state):  # Solution state reached
                print(str(node.state))
                return None

            while (node.depth < depth_cutoff):
                if (node.state == goal_state):  # Solution state reached
                    print(str(node.state))
                return None

            child_node = generate_solutions(node)


def generate_solutions(parent):
    input = parent.state
    next_iterations = []
    input_length = len(input)
  




if __name__ == '__main__':
    main()
