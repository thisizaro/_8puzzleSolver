# core/problem.py

from core.state import PuzzleState


class PuzzleProblem:
    def __init__(self, initial_board: tuple, goal_board: tuple = None):
        self.initial_state = PuzzleState(initial_board)
        self.goal_state = PuzzleState(
            goal_board if goal_board else PuzzleState.GOAL_STATE
        )

    def get_initial_state(self):
        return self.initial_state

    def is_goal(self, state):
        return state.board == self.goal_state.board

    def get_goal_state(self):
        return self.goal_state