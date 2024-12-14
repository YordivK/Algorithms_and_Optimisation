from collections import defaultdict, deque

def build_graph(input_data):
    graph = defaultdict(list)
    for edge in input_data[2:]:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)
    return graph

def restrict_graph(network, start_nodes, max_steps):
    visited = set(start_nodes)
    queue = deque([(node, 0) for node in start_nodes])
    restricted_network = defaultdict(list)

    while queue:
        node, steps = queue.popleft()
        if steps >= max_steps:
            continue

        for neighbor in network[node]:
            restricted_network[node].append(neighbor)  # Add edge to restricted graph
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))
    return restricted_network

def precompute_invalid_positions(network, min_D):
    invalid_positions = {}
    for u in network:
        invalid_positions[u] = set()
        queue = deque([(u, 0)])
        visited = {u}

        while queue:
            node, distance = queue.popleft()
            if distance >= min_D:
                continue

            for neighbor in network[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    invalid_positions[u].add(neighbor)
                    queue.append((neighbor, distance + 1))

    return invalid_positions