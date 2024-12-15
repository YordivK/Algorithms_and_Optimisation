# Read input, process the graph, and find socially distant paths

import time
from graph import build_graph, restrict_graph, precompute_invalid_positions
from bfs import bidirectional_socially_distant_paths

# Start tracking execution time for performance measurement
start_time = time.time()


# Input file reading (adjust the path to match your local setup)
# The file contains a graph and problem-specific parameters, formatted as:
# First line: n (nodes), m (edges), T (maximum steps), D (minimum distance)
# Second line: start and target nodes for two players (sa, ta, sb, tb)
# Subsequent lines: edges of the graph
input_file = "/Users/yordivankruchten/Downloads/testcases/grid50-9.in"
with open(input_file, "r") as f:
    lines = f.readlines()
input_data = [list(map(int, line.split())) for line in lines]

# Extract problem parameters
# n: number of nodes in the graph
# m: number of edges in the graph
# T: maximum number of steps allowed for any path
# D: minimum distance to be maintained between paths of the two players
n, m, T, D = input_data[0]

# Extract start and target nodes for the two players
# sa, ta: start and target nodes for player A
# sb, tb: start and target nodes for player B
sa, ta, sb, tb = input_data[1]

# Build the full graph from the input data
# The graph is represented as an adjacency list, where each node maps to a list of its neighbors
network = build_graph(input_data)

# Restrict the graph to nodes that are reachable within T steps from any of the critical nodes (start/target nodes)
# This step reduces the size of the graph, making subsequent computations more efficient
relevant_graph = restrict_graph(network, [sa, sb, ta, tb], T)

# Precompute invalid positions based on the minimum distance D
# For each node, identify the set of other nodes that cannot be visited simultaneously due to the distance constraint
invalid_positions = precompute_invalid_positions(relevant_graph, D)

# Use bidirectional BFS to compute the socially distant paths for the two players
# This algorithm ensures that paths are found (if they exist) while maintaining the minimum distance constraint
# Parameters:
# - relevant_graph: the reduced graph
# - (sa, ta, sb, tb): start and target nodes for the two players
# - T: maximum number of steps allowed
# - D: minimum distance to maintain between the paths
# - invalid_positions: precomputed invalid positions for efficiency
k, path_a, path_b = bidirectional_socially_distant_paths(
    relevant_graph, (sa, ta, sb, tb), T, D, invalid_positions
)

# Stop tracking execution time
end_time = time.time()

# Output the results
# k: the total time taken to complete the paths (or T+1 if no valid paths exist)
# path_a, path_b: the computed socially distant paths for player A and player B, respectively
print(k)
if path_a and path_b:
    # Print the paths as space-separated lists of node indices
    print(" ".join(map(str, path_a)))
    print(" ".join(map(str, path_b)))

# Print the total execution time for performance analysis
print(f"{end_time - start_time:.2f} seconds")