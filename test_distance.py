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
                return max_T + 1, None, None

    # Reconstruct the path from the parent map starting from the target node, and reverse.
    path_a = [target_a]
    parent_a = target_a
    if target_a in parent_map_a:
        while parent_a != start_a:
            path_a.append(parent_map_a[parent_a])
            parent_a = parent_map_a[parent_a]
        path_a.reverse()
    else:
        return max_T + 1, None, None


    return path_a

from graph import graph

with open("/Users/yordivankruchten/Downloads/testcases/grid10-5.in", "r") as file:
    lines = file.readlines()
input = [list(map(int, line.split())) for line in lines]
print(f"Minimum distance: {input[0][3]}")
start_target_list = input[1]
max_T = input[0][2]
min_D = input[0][3]

network = graph(input)
print(network)

test_start = 34
test_end = 7
path_a_test = bfs(network, [test_start, test_end, 1, 1], max_T, min_D)
if path_a_test != None:
    print(f"Shortest path from {test_start} to {test_end}: {path_a_test}. Length: {len(path_a_test)}.")
else:
    print(f"There is no path from {test_start} to {test_end}.")