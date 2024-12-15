from itertools import chain

def distance(graph, start, target):

    queue_a = [[start]]
    parent_map_a = {start: None}

    for layer in queue_a:
        new_layer = []
        for node in layer:
            for neighbor in graph[node]:
                if neighbor in chain.from_iterable(queue_a) or neighbor in new_layer:
                    continue
                    # If the neighbor is already in the queue or layer, don't add it to the next layer.

                parent_map_a[neighbor] = node

                if neighbor == target:
                    queue_a.append([neighbor])
                    break
                    # If the target is found by the algorithm, terminate the loop.

                new_layer.append(neighbor)
                # Add the neighbor to the new layer.

        if new_layer != []:
            queue_a.append(new_layer)
            # Add the new layer to the queue only if the new layer generates new nodes.

    # Reconstruct the path from the parent map starting from the target node, and reverse.
    path_a = [target]
    parent_a = target
    if target in parent_map_a:
        while parent_a != start:
            path_a.append(parent_map_a[parent_a])
            parent_a = parent_map_a[parent_a]
        path_a.reverse()
    else:
        return float('inf')


    return len(path_a)