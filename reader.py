with open("/Users/yordivankruchten/Downloads/testcases/case1.in", "r") as file:
    # Split the content into lines
    lines = file.readlines()

# Split each line into individual numbers and convert them to integers
input = [list(map(int, line.split())) for line in lines]

# First line breakdown
n = input[0][0]
print(f"Number of vertices (n) = {n}")
m = input[0][1]
print(f"Number of edges (m) = {m}")
T = input[0][2]
print(f"Maximum time (T) = {T}")
D = input[0][3]
print(f"Minimum distance (D) = {D}")
print()

# Second line breakdown
s_a = input[1][0]
print(f"Starting point of player a (s_a) = {s_a}")
t_a = input[1][1]
print(f"Target point of player a (t_a) = {t_a}")
s_b = input[1][2]
print(f"Starting point of player b (s_b) = {s_b}")
t_b = input[1][3]
print(f"Target point of player b (t_b) = {t_b}")
print()

# Edge breakdown
edges = len(input)
for i in range(2, edges):
    edge_start = input[i][0]
    edge_end = input[i][1]
    print(f"Edge {i-1} from vertex {edge_start} to {edge_end}")