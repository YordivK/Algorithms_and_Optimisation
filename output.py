import time
from graph import build_graph, restrict_graph, precompute_invalid_positions
from bfs import bidirectional_socially_distant_paths

start_time = time.time()

def main():
    # Read input from a file
    input_file = "/Users/flipv/OneDrive/Documents/ALGOPT/testcases/grid50-0.in"
    with open(input_file, "r") as f:
        lines = f.readlines()
    input_data = [list(map(int, line.split())) for line in lines]

    # Extract parameters
    n, m, T, D = input_data[0]
    sa, ta, sb, tb = input_data[1]

    # Build graph
    network = build_graph(input_data)

    # Restrict graph to relevant nodes
    relevant_graph = restrict_graph(network, [sa, sb, ta, tb], T)

    # Precompute invalid positions
    invalid_positions = precompute_invalid_positions(relevant_graph, D)

    # Run the bidirectional BFS algorithm
    k, path_a, path_b = bidirectional_socially_distant_paths(
        relevant_graph, (sa, ta, sb, tb), T, D, invalid_positions
    )
    end_time = time.time()

    # Output results
    print(k)
    if path_a and path_b:
        print(" ".join(map(str, path_a)))
        print(" ".join(map(str, path_b)))
    print(f"{end_time - start_time:.2f} seconds")    

if __name__ == "__main__":
    main()
