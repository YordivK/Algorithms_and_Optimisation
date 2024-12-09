from itertools import chain

def bfs(graph, start_target_list, max_T, min_D):

    start_a = start_target_list[0]
    target_a = start_target_list[1]
    queue_a = [[start_a]]
    parent_map_a = {start_a: None}

    for layer in queue_a:
        new_layer = []
        for node in layer:
            for neighbor in graph[node]:
                if neighbor in chain.from_iterable(queue_a) or neighbor in new_layer:
                    continue
                    # If the neighbor is already in the queue or layer, don't add it to the next layer.

                parent_map_a[neighbor] = node

                if neighbor == target_a:
                    queue_a.append([neighbor])
                    break
                    # If the target is found by the algorithm, terminate the loop.

                new_layer.append(neighbor)
                # Add the neighbor to the new layer.

        if new_layer != []:
            queue_a.append(new_layer)
            # Add the new layer to the queue only if the new layer generates new nodes.

            if len(queue_a) >= max_T:
                return max_T + 1

    # Reconstruct the path from the parent map starting from the target node, and reverse.
    path_a = [target_a]
    parent_a = target_a
    if target_a in parent_map_a:
        while parent_a != start_a:
            path_a.append(parent_map_a[parent_a])
            parent_a = parent_map_a[parent_a]
        path_a.reverse()
    else:
        return max_T + 1



    start_b = start_target_list[2]
    target_b = start_target_list[3]
    queue_b = [[start_b]]
    parent_map_b = {start_b: []}
    # Since there can be cycles in the path of player b, due to keeping distance from player a,
    # we need to be able to save multiple parents to reconstruct the path,
    # therefore we need to use lists as the values of the dictionary parent_map_b.

    found = False
    for layer in queue_b:
        new_layer = []

        # The block of code below calculates the forbidden nodes:
        # the nodes that are not allowed according to the minimum distance
        # to the current position of player a
        step = len(queue_b) # step gives in which layer we are
        pos_a = path_a[step if step <= len(path_a)-1 else len(path_a)-1] # pos_a gives the position of player a, when player b moves from layer 'step'
        k = min_D
        forbidden = [pos_a]
        forbidden_nodes = [pos_a]
        while k > 0:
            for node in forbidden:
                existing = set(forbidden_nodes) # Use a set to avoid duplicates efficiently
                forbidden_nodes.extend(item for item in graph[node] if item not in existing)
                forbidden = graph[node]
                k = k - 1

        min_D_graph = {key: [node for node in value if node not in forbidden_nodes] for key, value in graph.items()}
        # This updated graph deletes all nodes that are not allowed
        # due to the minimum distance requirement. In each time step
        # counted for every new layer that is added to queue_b,
        # the updated graph is reevaluated from the original graph,
        # deleting only the nodes that are not allowed due to the
        # position of player a at that time step.

        for node in layer:
            for neighbor in min_D_graph[node]:
                if neighbor in new_layer:
                    continue
                    # If the neighbor is already in the layer, don't add it to the next layer.

                if neighbor in parent_map_b:
                    parent_map_b[neighbor].append(node)
                else:
                    parent_map_b[neighbor] = [node]

                if neighbor == target_b:
                    queue_b.append([neighbor])
                    found = True
                    break
                    # If the target is found by the algorithm, terminate the loop.

                new_layer.append(neighbor)
                # Add the neighbor to the new layer.

        if found:
            break
        elif new_layer != []:
            queue_b.append(new_layer)
            # Add the new layer to the queue only if the new layer generates new nodes.

            if len(queue_b) >= max_T:
                return max_T + 1

    # Reconstruct the path from the parent map starting from the target node, and reverse.
    path_b = [target_b]
    parent_b = target_b
    count = step
    if target_b in parent_map_b:
        while count > 0:
            path_b.append(parent_map_b[parent_b][0])
            parent_b = parent_map_b[parent_b][0]
            count = count - 1
            #if count == 0 and path_b[-1] != start_b:

        path_b.reverse()
    else:
        return max_T + 1

    k = max(len(path_a), len(path_b)) - 1

    return k, path_a, path_b