def bfs(graph, start_target_list, max_T):

    queue_a = [[start_target_list[0], None]]
    for queue_item in queue_a:
        node = queue_item[0]
        for neighbor in graph[node]:
            check = False
            for queued_nodes in queue_a:
                if queued_nodes[0] == neighbor:
                    check = True
            if check:
                continue
                # If the neighbor already exists, don't add it to the queue again.
            elif neighbor == start_target_list[1]:
                queue_a.append([neighbor, node])
                break
                # If the target is found by the algorithm, terminate the loop.
            else:
                queue_a.append([neighbor, node])
                # Add the neighbor to the queue and also save where it came from (node) to later reconstruct the path.


    queue_b = [[start_target_list[2], None]]
    for queue_item in queue_b:
        node = queue_item[0]
        for neighbor in graph[node]:
            check = False
            for queued_nodes in queue_b:
                if queued_nodes[0] == neighbor:
                    check = True
            if check:
                continue
                # If the neighbor already exists, don't add it to the queue again.
            elif neighbor == start_target_list[1]:
                queue_b.append([neighbor, node])
                break
                # If the target is found by the algorithm, terminate the loop.
            else:
                queue_b.append([neighbor, node])
                # Add the neighbor to the queue and also save where it came from (node) to later reconstruct the path.

    # The path list contains the path from start to target, according to the bfs algorithm.
    path_a = [start_target_list[1]]
    for paths in path_a:
        for sub in queue_a:
            if sub[0] == paths:
                path_a.append(sub[1])

    # The path list contains the path from start to target, according to the bfs algorithm.
    path_b = [start_target_list[3]]
    for paths in path_b:
        for sub in queue_b:
            if sub[0] == paths:
                path_b.append(sub[1])

    # Pop off the value None from the start node.
    # Reverse the list, so that the path goes from start to target.
    path_a.pop()
    final_path_a = list(reversed(path_a))
    path_b.pop()
    final_path_b = list(reversed(path_b))

    if final_path_a == [] and final_path_b == []:
        return "There exists no path from start to target for both player a and b."
    elif len(path_a) > max_T:
        return f"There is no path within maximum time {max_T}."
    else:
        return final_path_a, final_path_b