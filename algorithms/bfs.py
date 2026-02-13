# algorithms/bfs.py

import time
from collections import deque
from core.node import Node


def solve(problem):
    start_time = time.time()

    initial_state = problem.get_initial_state()
    root = Node(initial_state)

    frontier = deque([root])
    visited = set()
    visited.add(initial_state)

    trace = []
    nodes_expanded = 0
    max_frontier_size = 1
    step = 0

    while frontier:
        max_frontier_size = max(max_frontier_size, len(frontier))

        current_node = frontier.popleft()
        nodes_expanded += 1
        step += 1

        if problem.is_goal(current_node.state):
            end_time = time.time()
            solution_path = current_node.reconstruct_path()

            return {
                "solution_path": solution_path,
                "trace": trace,
                "metrics": {
                    "nodes_expanded": nodes_expanded,
                    "max_frontier_size": max_frontier_size,
                    "solution_depth": current_node.depth,
                    "path_cost": current_node.g,
                    "execution_time": end_time - start_time,
                },
            }

        generated_children = []

        for move, neighbor_state in current_node.state.get_neighbors():
            if neighbor_state not in visited:
                visited.add(neighbor_state)

                child_node = Node(
                    state=neighbor_state,
                    parent=current_node,
                    move=move,
                    g=current_node.g + 1,
                )

                frontier.append(child_node)
                generated_children.append(child_node)

        chosen_node = frontier[0] if frontier else None

        trace.append({
            "step": step,
            "expanded": current_node,
            "generated": generated_children,
            "chosen": chosen_node,
            "frontier_size": len(frontier),
        })

    return None  # No solution