# algorithms/registry.py

from algorithms.bfs import solve as bfs_solve
# from algorithms.dfs import solve as dfs_solve
# from algorithms.best_first import solve as bestfs_solve
# from algorithms.a_star import solve as astar_solve

# Registry dictionary
ALGORITHMS = {
    "BFS": ("Breadth-First Search", bfs_solve),
    # "DFS": ("Depth-First Search", dfs_solve),
    # "BestFS": ("Best First Search", bestfs_solve),
    # "A*": ("A* Search", astar_solve),
}