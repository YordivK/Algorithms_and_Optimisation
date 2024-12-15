from collections import defaultdict, deque

def build_graph(input_data):
    # Constructs an undirected graph from the given input data.
    # Each edge is bi-directional, representing connectivity between two vertices.

    graph = defaultdict(list)
    for edge in input_data[2:]: # Skip the first two lines (parameters and start/target nodes: leaves only edges)
        u, v = edge
        # Add both directions to ensure the graph is undirected
        graph[u].append(v)
        graph[v].append(u)
    return graph

def restrict_graph(network, start_nodes, max_steps):
    # Restricts the graph to nodes that are reachable from the given start nodes within max_steps.
    # This avoids exploring unnecessary nodes that are too far away to be part of a valid solution.

    visited = set(start_nodes) # Keep track of visited nodes to prevent revisiting
    queue = deque([(node, 0) for node in start_nodes]) # Initialize the queue with start nodes and step 0
    restricted_network = defaultdict(list)

    while queue:
        node, steps = queue.popleft()
        if steps >= max_steps: # Stop exploring if we've reached the maximum allowed distance
            continue

        for neighbor in network[node]:
            restricted_network[node].append(neighbor)  # Add the edge to the restricted network
            if neighbor not in visited: # Explore unvisited neighbors
                visited.add(neighbor)
                queue.append((neighbor, steps + 1)) # Increment the step count
    return restricted_network

def precompute_invalid_positions(network, min_D):
    # Precomputes invalid positions for each node, ensuring that two players are always at least
    # min_D steps apart. This helps enforce the social distance constraint during the main search.

    invalid_positions = {}
    for u in network:
        invalid_positions[u] = set()  # For each node, store nodes that violate the min_D constraint
        queue = deque([(u, 0)]) # Start BFS from the current node
        visited = {u}

        while queue:
            node, distance = queue.popleft()
            if distance >= min_D: # Stop exploring neighbors beyond the minimum distance
                continue

            for neighbor in network[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    invalid_positions[u].add(neighbor) # Mark the neighbor as invalid
                    queue.append((neighbor, distance + 1)) # Increment the distance

    return invalid_positions