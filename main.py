# main.py

import sys
from utils.loader import list_maps, load_map
from utils.solvability import is_solvable
from core.problem import PuzzleProblem
from visualization.cli_renderer import CLIRenderer
from algorithms.registry import ALGORITHMS


def select_map():
    maps = list_maps()
    if not maps:
        print("No maps found in maps/ folder.")
        sys.exit(1)

    print("Available maps:")
    for idx, m in enumerate(maps, 1):
        print(f"{idx}. {m}")

    while True:
        choice = input("Select a map by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(maps):
            return maps[int(choice) - 1]
        else:
            print("Invalid choice. Try again.")


def select_algorithm():
    print("\nAvailable algorithms:")
    for key, (name, _) in enumerate(ALGORITHMS.items(), 1):
        print(f"{key}. {name}")

    while True:
        choice = input("Select an algorithm by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(ALGORITHMS):
            selected_key = list(ALGORITHMS.keys())[int(choice) - 1]
            return selected_key
        else:
            print("Invalid choice. Try again.")


def main():
    print("=== 8-Puzzle Solver ===\n")

    # Select map
    map_file = select_map()
    board = load_map(f"maps/{map_file}")

    if not is_solvable(board):
        print("\nThis puzzle is NOT solvable. Exiting.")
        sys.exit(0)

    problem = PuzzleProblem(board)

    # Select algorithm
    algo_key = select_algorithm()
    algo_name, algo_func = ALGORITHMS[algo_key]

    print(f"\nRunning {algo_name} on {map_file}...\n")

    # Solve
    result = algo_func(problem)

    # Render CLI
    renderer = CLIRenderer(delay=0.3)
    for step_data in result['trace']:
        renderer.render_step(step_data)

    renderer.render_solution(result['solution_path'])
    renderer.render_metrics(result['metrics'])


if __name__ == "__main__":
    main()