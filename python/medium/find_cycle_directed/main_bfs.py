from collections import deque, defaultdict


def has_cycle_bfs(num_nodes, edges):
    graph = defaultdict(list)
    in_degree = [0] * num_nodes

    # Build graph and in-degree array
    for a, b in edges:
        graph[a].append(b)
        in_degree[b] += 1

    # Start with nodes having in-degree 0
    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    visited = 0

    while queue:
        node = queue.popleft()
        visited += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return visited != num_nodes  # True if cycle exists
