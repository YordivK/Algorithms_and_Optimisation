# bfs.py
from collections import deque

def bidirectional_socially_distant_paths(network, start_target_list, max_T, min_D, invalid_positions):
    """
    Find socially distant paths using bidirectional BFS.

    Args:
        network (dict): The adjacency list of the graph.
        start_target_list (tuple): Start and target nodes (sa, ta, sb, tb).
        max_T (int): Maximum allowed time.
        min_D (int): Minimum distance between players.
        invalid_positions (dict): Precomputed invalid positions for each node.

    Returns:
        tuple: (k, path_a, path_b) where k is the time, path_a and path_b are the paths.
    """
    sa, ta, sb, tb = start_target_list

    # Forward and backward queues
    forward_q = deque([(sa, sb, 0)])
    backward_q = deque([(ta, tb, 0)])

    # Visited sets for forward and backward
    forward_visited = set([(sa, sb, 0)])
    backward_visited = set([(ta, tb, 0)])

    # Parent dictionaries for path reconstruction
    forward_parent = {}
    backward_parent = {}

    meeting_state = None

    while forward_q or backward_q:
        # Expand forward queue
        if forward_q:
            pa, pb, t = forward_q.popleft()
            if (pa, pb, t) in backward_visited:
                meeting_state = (pa, pb, t)
                break

            if t < max_T:
                for pa_next in [pa] + network[pa]:
                    for pb_next in [pb] + network[pb]:
                        # Ensure the players are not at the same node at the same time
                        if pa_next == pb_next:
                            continue
                        # Skip if the move violates the invalid positions
                        if pb_next in invalid_positions[pa_next]:
                            continue
                        if (pa_next, pb_next, t + 1) not in forward_visited:
                            forward_visited.add((pa_next, pb_next, t + 1))
                            forward_parent[(pa_next, pb_next, t + 1)] = (pa, pb, t)
                            forward_q.append((pa_next, pb_next, t + 1))

        # Expand backward queue
        if backward_q:
            pa, pb, t = backward_q.popleft()
            if (pa, pb, t) in forward_visited:
                meeting_state = (pa, pb, t)
                break

            if t < max_T:
                for pa_next in [pa] + network[pa]:
                    for pb_next in [pb] + network[pb]:
                        # Ensure the players are not at the same node at the same time
                        if pa_next == pb_next:
                            continue
                        # Skip if the move violates the invalid positions
                        if pb_next in invalid_positions[pa_next]:
                            continue
                        if (pa_next, pb_next, t + 1) not in backward_visited:
                            backward_visited.add((pa_next, pb_next, t + 1))
                            backward_parent[(pa_next, pb_next, t + 1)] = (pa, pb, t)
                            backward_q.append((pa_next, pb_next, t + 1))

    if meeting_state:
        return reconstruct_bidirectional_path(sa, sb, ta, tb, forward_parent, backward_parent, meeting_state)

    return max_T + 1, None, None

def reconstruct_bidirectional_path(sa, sb, ta, tb, forward_parent, backward_parent, meeting_state):
    """
    Reconstruct the bidirectional paths for two players, avoiding redundant "double values."

    Args:
        sa, sb (int): Starting nodes for player A and B.
        ta, tb (int): Target nodes for player A and B.
        forward_parent (dict): Parent mapping from forward BFS.
        backward_parent (dict): Parent mapping from backward BFS.
        meeting_state (tuple): The state where forward and backward searches met.

    Returns:
        tuple: (k, path_a, path_b) where k is the meeting time, path_a and path_b are the paths.
    """
    pa_meet, pb_meet, k = meeting_state

    # Reconstruct path for player A and B from forward BFS
    forward_path_a = []
    forward_path_b = []
    current_state = (pa_meet, pb_meet, k)
    while current_state in forward_parent:
        pa, pb, t = current_state
        forward_path_a.append(pa)
        forward_path_b.append(pb)
        current_state = forward_parent[current_state]
    forward_path_a.append(sa)
    forward_path_b.append(sb)
    forward_path_a.reverse()
    forward_path_b.reverse()

    # Reconstruct path for player A and B from backward BFS
    backward_path_a = []
    backward_path_b = []
    current_state = (pa_meet, pb_meet, k)
    while current_state in backward_parent:
        pa, pb, t = backward_parent[current_state]
        backward_path_a.append(pa)
        backward_path_b.append(pb)
        current_state = backward_parent[current_state]
    backward_path_a.append(ta)
    backward_path_b.append(tb)

    # Combine forward and backward paths
    path_a = forward_path_a + backward_path_a
    path_b = forward_path_b + backward_path_b

    # Filter out redundant double values
    filtered_path_a = [path_a[0]]
    filtered_path_b = [path_b[0]]
    for i in range(1, len(path_a)):
        if not (path_a[i] == path_a[i - 1] and path_b[i] == path_b[i - 1]):
            filtered_path_a.append(path_a[i])
            filtered_path_b.append(path_b[i])

    # The length of the filtered paths determines the meeting time
    meeting_time = len(filtered_path_a) - 1

    return meeting_time, filtered_path_a, filtered_path_b