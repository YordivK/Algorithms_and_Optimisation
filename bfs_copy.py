from audioop import reverse
from itertools import chain

def bfs(graph, start_target_list, max_T):

    queue_a = [[start_target_list[0]]]
    parent_map_a = {start_target_list[0]: None}
    for layer in queue_a:
        new_layer = []
        for node in layer:
            for neighbor in graph[node]:

                if neighbor == start_target_list[1]:
                    queue_a.append([neighbor])
                    break
                    # If the target is found by the algorithm, terminate the loop.

                elif neighbor in chain.from_iterable(queue_a):
                    continue
                    # If the neighbor is already in the queue, don't add it to the next layer.

                elif neighbor not in new_layer:
                    new_layer.append(neighbor)
                    parent_map_a[node] = neighbor
                    # Add the neighbor to the new layer, if it wasn't already.

        if new_layer != []:
            queue_a.append(new_layer)
            # Add the new layer to the queue only if the new layer generates new nodes.

            if len(queue_a) == max_T:
                return f"No path could be found within maximum time {max_T}."

    #if:
    #else:
        #return "No path could be found from start to target."


    return parent_map_a, queue_a