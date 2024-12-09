from itertools import chain

def bfs(graph, start_target_list, max_T):

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
                return f"No path could be found within maximum time {max_T}."

    # Reconstruct the path from the parent map starting from the target node, and reverse.
    path_a = [target_a]
    parent_a = target_a
    if target_a in parent_map_a:
        while parent_a != start_a:
            path_a.append(parent_map_a[parent_a])
            parent_a = parent_map_a[parent_a]
        path_a.reverse()
    else:
        return "No path could be found from start to target."



    start_b = start_target_list[2]
    target_b = start_target_list[3]
    queue_b = [[start_b]]
    parent_map_b = {start_b: None}

    for layer in queue_b:
        new_layer = []
        for node in layer:
            for neighbor in graph[node]:
                if neighbor in chain.from_iterable(queue_b) or neighbor in new_layer:
                    continue
                    # If the neighbor is already in the queue or layer, don't add it to the next layer.

                parent_map_b[neighbor] = node

                if neighbor == target_b:
                    queue_b.append([neighbor])
                    break
                    # If the target is found by the algorithm, terminate the loop.

                new_layer.append(neighbor)
                # Add the neighbor to the new layer.

        if new_layer != []:
            queue_b.append(new_layer)
            # Add the new layer to the queue only if the new layer generates new nodes.

            if len(queue_b) >= max_T:
                return f"No path could be found within maximum time {max_T}."

    # Reconstruct the path from the parent map starting from the target node, and reverse.
    path_b = [target_b]
    parent_b = target_b
    if target_b in parent_map_b:
        while parent_b != start_b:
            path_b.append(parent_map_b[parent_b])
            parent_b = parent_map_b[parent_b]
        path_b.reverse()
    else:
        return "No path could be found from start to target."



    return path_a, path_b