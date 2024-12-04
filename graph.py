from collections import defaultdict

def graph(input):

    # Create a dictionary that contains keys being all vertices, and values being their neighbors
    graph = defaultdict(dict)
    for vertex in range(1, input[0][0]+1):
        graph[vertex] = []
    length = len(input)
    for i in range(2, length):
        graph[input[i][0]].append(input[i][1])
        graph[input[i][1]].append(input[i][0])

    return graph