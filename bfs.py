from collections import deque

def bfs(graph, start, goal):
    # Keep track of visited nodes
    visited = set()

    # Create a queue to store nodes that are waiting to be processed
    queue = deque([start])

    # Loop until the queue is empty
    while queue:
        # Get the next node from the queue
        node = queue.popleft()

        # If the node has not been visited before, process it
        if node not in visited:
            # Mark the node as visited
            visited.add(node)

            # If the node is the goal, return True
            if node == goal:
                return f"yes  {goal} node is founded in tree and neighbors are {graph[node]}"

            # Get the neighbors of the node
            neighbors = graph[node]

            # Add the neighbors to the queue
            queue.extend(neighbors)

    # If we get here, the goal was not found
    return f"Sorry Goal Node {goal} is not Exist in tree "

# Test the BFS function
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}
Goal_node = input("enter your Goal Node: ")
print(bfs(graph, 'A', Goal_node))  # True
# print(bfs(graph, 'A', 'G'))  # False