def dfs(graph, start, goal):
    # Keep track of visited nodes
    visited = set()

    # Create a stack to store nodes that are waiting to be processed
    stack = [start]

    # Loop until the stack is empty
    while stack:
        # Get the next node from the stack
        node = stack.pop()

        # If the node has not been visited before, process it
        if node not in visited:
            # Mark the node as visited
            visited.add(node)

            # If the node is the goal, return True
            if node == goal:
                return f"yes its present in tree and neightbors nodes are {graph[node]}"

            # Get the neighbors of the node
            neighbors = graph[node]

            # Add the neighbors to the stack
            stack.extend(neighbors)

    # If we get here, the goal was not found
    return f"Sorry we can find your Goal Node {goal}."

# Test the DFS function
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
print(graph)
goal_node = input("enter your Goal Node: ")
print(dfs(graph, 'A', goal_node)) 

