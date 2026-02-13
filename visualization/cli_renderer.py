# visualization/cli_renderer.py

import time


class CLIRenderer:
    def __init__(self, delay=0.5):
        """
        delay: seconds between steps for visualization
        """
        self.delay = delay

    def render_board(self, state):
        """
        Render a PuzzleState using ASCII art.
        """
        print(state)

    def render_step(self, step_data):
        """
        Render a single expansion step.
        step_data: dict from trace
        """
        print("\n" + "=" * 40)
        print(f"STEP {step_data['step']}")
        print(f"Frontier size: {step_data['frontier_size']}")
        print("\nExpanded Node:")
        self.render_board(step_data['expanded'].state)

        if step_data['generated']:
            print("\nGenerated Children:")
            for idx, child in enumerate(step_data['generated'], 1):
                print(f"\nChild {idx} (Move: {child.move}, g={child.g}):")
                self.render_board(child.state)
        else:
            print("\nNo children generated.")

        if step_data['chosen']:
            print(f"\n>>> Chosen Node for next expansion: Move {step_data['chosen'].move}")
        print("=" * 40)
        time.sleep(self.delay)

    def render_solution(self, solution_path):
        """
        Render the final solution path step by step.
        """
        print("\n" + "#" * 40)
        print("SOLUTION PATH")
        for idx, node in enumerate(solution_path, 1):
            print(f"\nStep {idx} (Move: {node.move}, g={node.g})")
            self.render_board(node.state)
            time.sleep(self.delay)
        print("#" * 40 + "\n")

    def render_metrics(self, metrics):
        """
        Render final statistics.
        """
        print("\n" + "=" * 50)
        print("SOLUTION METRICS")
        for key, value in metrics.items():
            if isinstance(value, float):
                print(f"{key.replace('_', ' ').title()}: {value:.4f}")
            else:
                print(f"{key.replace('_', ' ').title()}: {value}")
        print("=" * 50 + "\n")