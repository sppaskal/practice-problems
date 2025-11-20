from collections import deque, defaultdict


def has_cycle_undirected_bfs(num_nodes, edges):
    # Step 1: Build the adjacency list representation of the graph.
    # Each node maps to a list of its neighbors.
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)  # Since the graph is undirected, add both directions.

    # Step 2: Track visited nodes to avoid revisiting and to handle disconnected components.
    visited = [False] * num_nodes

    # Step 3: Iterate through all nodes to ensure we cover disconnected components.
    for start in range(num_nodes):
        if not visited[start]:
            # Step 3a: Start BFS from this unvisited node.
            # We store (node, parent) in the queue to track where we came from.
            queue = deque([(start, -1)])
            visited[start] = True  # Mark the start node as visited.

            # Step 3b: Standard BFS loop.
            while queue:
                current, parent = queue.popleft()

                # Step 3c: Explore all neighbors of the current node.
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        # If the neighbor hasn't been visited, mark it and enqueue it.
                        visited[neighbor] = True
                        queue.append((neighbor, current))  # Track current as parent.
                    elif neighbor != parent:
                        # If the neighbor is visited and is NOT the parent,
                        # we've found a back edge → cycle detected.
                        return True

    # Step 4: If we finish BFS for all components without finding a cycle, return False.
    return False
