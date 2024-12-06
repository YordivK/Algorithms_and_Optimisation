from graph import graph
from bfs import bfs

with open("/Users/yordivankruchten/Downloads/testcases/case0.in", "r") as file:
    lines = file.readlines()
input = [list(map(int, line.split())) for line in lines]
print(input)
start = input[1][0]
print(f"Start = {start}")
target = input[1][1]
print(f"Target = {target}")
max_T = input[0][2]
print(f"Maximum time = {max_T}")

network = graph(input)
print(network)

print(bfs(network, start, target, max_T))