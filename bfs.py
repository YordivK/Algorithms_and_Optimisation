from collections import deque

def bidirectional_socially_distant_paths(network, start_target_list, max_T, min_D, invalid_positions):
    sa, ta, sb, tb = start_target_list

    # Forward and backward queues
    forward_queue = deque([(sa, sb, 0)])  # (position_a, position_b, time)
    backward_queue = deque([(ta, tb, 0)])  # (position_a, position_b, time)

    # Visited states with distances
    forward_visited = {(sa, sb): 0}
    backward_visited = {(ta, tb): 0}

    # Parent dictionaries for reconstructing paths
    forward_parent = {}
    backward_parent = {}

    def expand(queue, visited, parent, other_visited, current_invalid_positions):
        if not queue:
            return None

        best_meeting_state = None
        best_total_time = float('inf')

        for _ in range(len(queue)):  # Process the current level of the queue
            current_pa, current_pb, current_time = queue.popleft()

            if (current_pa, current_pb) in other_visited:
                total_time = current_time + other_visited[(current_pa, current_pb)]
                if total_time < best_total_time:
                    best_total_time = total_time
                    best_meeting_state = (current_pa, current_pb, total_time)

            if current_time >= max_T:
                continue

            for pa_next in network[current_pa]:  # Only consider moving actions
                for pb_next in network[current_pb]:
                    if pa_next == pb_next or pb_next in current_invalid_positions.get(pa_next, set()):
                        continue

                    new_state = (pa_next, pb_next)
                    if new_state not in visited or visited[new_state] > current_time + 1:
                        visited[new_state] = current_time + 1
                        parent[new_state] = (current_pa, current_pb)
                        queue.append((pa_next, pb_next, current_time + 1))

        return best_meeting_state

    while forward_queue or backward_queue:
        if forward_queue:
            meeting_state = expand(
                forward_queue, forward_visited, forward_parent,
                backward_visited, invalid_positions
            )
            if meeting_state:
                return reconstruct_bidirectional_path(sa, sb, ta, tb, forward_parent, backward_parent, meeting_state)

        if backward_queue:
            meeting_state = expand(
                backward_queue, backward_visited, backward_parent,
                forward_visited, invalid_positions
            )
            if meeting_state:
                return reconstruct_bidirectional_path(sa, sb, ta, tb, forward_parent, backward_parent, meeting_state)

    return max_T + 1, None, None


def reconstruct_bidirectional_path(sa, sb, ta, tb, forward_parent, backward_parent, meeting_state):
    """
    Reconstructs the paths for two players from start to target through the meeting state.

    Args:
        sa, sb: Starting nodes for player A and player B.
        ta, tb: Target nodes for player A and player B.
        forward_parent: Parent mapping from forward BFS.
        backward_parent: Parent mapping from backward BFS.
        meeting_state: The meeting state (pa_meet, pb_meet, meeting_time).

    Returns:
        Tuple (k, path_a, path_b):
            - k is the total time to reach the target.
            - path_a is the list of nodes for player A.
            - path_b is the list of nodes for player B.
    """
    pa_meet, pb_meet, meeting_time = meeting_state

    # Forward path reconstruction
    path_a_forward, path_b_forward = [], []
    current_state = (pa_meet, pb_meet)
    while current_state in forward_parent:
        pa, pb = forward_parent[current_state]
        path_a_forward.append(pa)
        path_b_forward.append(pb)
        current_state = (pa, pb)

    path_a_forward.reverse()
    path_b_forward.reverse()

    # Backward path reconstruction
    path_a_backward, path_b_backward = [], []
    current_state = (pa_meet, pb_meet)
    while current_state in backward_parent:
        pa, pb = backward_parent[current_state]
        path_a_backward.append(pa)
        path_b_backward.append(pb)
        current_state = (pa, pb)

    path_a_backward.append(ta)
    path_b_backward.append(tb)

    # Combine paths
    full_path_a = path_a_forward + [pa_meet] + path_a_backward
    full_path_b = path_b_forward + [pb_meet] + path_b_backward

    # Synchronize lengths
    max_length = max(len(full_path_a), len(full_path_b))
    while len(full_path_a) < max_length:
        full_path_a.append(full_path_a[-1])
    while len(full_path_b) < max_length:
        full_path_b.append(full_path_b[-1])

    # Remove redundant trailing nodes
    while len(full_path_a) > 1 and full_path_a[-1] == full_path_a[-2]:
        full_path_a.pop()
    while len(full_path_b) > 1 and full_path_b[-1] == full_path_b[-2]:
        full_path_b.pop()

    return meeting_time, full_path_a, full_path_b
