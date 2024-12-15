Give a (brief) high-level description of your algorithm

The graph.py file:
1.	Build the full graph using build_graph.
2.	Restrict the graph to relevant nodes with restrict_graph.
3.	Precompute invalid positions for social distance constraints using precompute_invalid_positions.

The BFS.py file: 
1. Run bidirectional BFS with bidirectional_socially_distant_paths.
2. Expand BFS states with expand during each iteration.
3. Reconstruct the paths with reconstruct_bidirectional_path once a meeting state is found.

The output file combines these functions and prints the output with the computation time.

Justify the correctness of your algorithm

This is a valid and optimal algorithm, as it is based on bidirectional BFS, an efficient way to find the shortest path by searching both from the start and towards the target. 
It ensures that both players are not within D distance from each other and it makes sure the time constraint is satisfied, by precomputing the invalid positions and filtering out invalid moves during the search. 
The visited states ensure that no state is processed more than once, and the paths are correctly reconstructed by combining the forward and backward searches at the meeting point, thus guaranteeing a valid and optimal solution.