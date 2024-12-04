def bfs(graph, start, target):

    queue = [[start, None]]
    for queue_item in queue:
        node = queue_item[0]
        for neighbor in graph[node]:
            check = False
            for queued_nodes in queue:
                if queued_nodes[0] == neighbor:
                    check = True
            if check:
                continue
                # If the neighbor already exists, don't add it to the queue again.
            elif neighbor == target:
                queue.append([neighbor, node])
                break
                # If the target is found by the algorithm, terminate the loop.
            else:
                queue.append([neighbor, node])
                # Add the neighbor to the queue and also save where it came from (node) to later find the path.

    # The path list contains the path from start to target, according to the bfs algorithm.
    path = [target]
    for paths in path:
        for sub in queue:
            if sub[0] == paths:
                path.append(sub[1])

    # Pop off the value None from the start node.
    # Reverse the list, so that the path goes from start to target.
    path.pop()
    final_path = list(reversed(path))

    if final_path == []:
        return "There exists no path from start to target."
    else:
        return final_path