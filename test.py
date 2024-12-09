from graph import graph
from bfs_copy import bfs

with open("/Users/yordivankruchten/Downloads/testcases/case0.in", "r") as file:
    lines = file.readlines()
input = [list(map(int, line.split())) for line in lines]
print(input)
start_target_list = input[1]
print(f"Start player a = {start_target_list[0]}")
print(f"Target player a = {start_target_list[1]}")
print(f"Start player b = {start_target_list[2]}")
print(f"Target player b = {start_target_list[3]}")
max_T = input[0][2]
print(f"Maximum time = {max_T}")
min_D = input[0][3]
print(f"Minimum distance = {min_D}")

network = graph(input)
print(network)

print(bfs(network, start_target_list, max_T))