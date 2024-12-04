from graph import graph

with open("/Users/yordivankruchten/Downloads/testcases/case0.in", "r") as file:
    lines = file.readlines()
input = [list(map(int, line.split())) for line in lines]

print(graph(input))

#def bfs(network):
#
#    queue = [['source', None]]
#    for queue_item in queue:
#        node = queue_item[0]
#        for neighbor in network[node].items():
#            check = False
#            for queued_nodes in queue:
#                if queued_nodes[0] == neighbor:
#                    check = True
#            if check:
#                continue
#                # If the neighbor already exists, don't add it to the queue again.
#                # If the residual flow of this node, neighbor pair is zero, don't add it to the queue
#            elif neighbor == 'sink':
#                queue.append([neighbor, node])
#                break
#                # If the sink is found by the algorithm, terminate the loop.
#            else:
#                queue.append([neighbor, node])
#                # Add the neighbor to the queue and also save where it came from (node) to later find the path.

    # The path list contains the path from source to sink, according to the bfs algorithm.
#    path = ['sink']
#    for paths in path:
#        for sub in queue:
#            if sub[0] == paths:
#                path.append(sub[1])

    # Pop off the value None from the source node.
    # Reverse the list, so that the path goes from source to sink.
#    path.pop()
#    final_path = list(reversed(path))

#    if final_path == []:
#        return "No more paths could be found from source to sink."
#    else:
#        return final_path