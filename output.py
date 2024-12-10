import time

# Record the start time
start_time = time.time()

from graph import graph
from bfs import bfs

with open("/Users/yordivankruchten/Downloads/testcases/grid10-5.in", "r") as file:
    lines = file.readlines()
input = [list(map(int, line.split())) for line in lines]

start_target_list = input[1]
max_T = input[0][2]
min_D = input[0][3]

network = graph(input)

k, path_a, path_b = bfs(network, start_target_list, max_T, min_D)

print(k)
if path_a and path_b != None:
    print(*path_a)
    print(*path_b)

# Record the end time
end_time = time.time()

# Calculate the duration
duration = end_time - start_time

# Print the time taken
print(f"{duration:.2f} seconds")