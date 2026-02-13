# core/state.py

class PuzzleState:
    GOAL_STATE = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    def __init__(self, board: tuple):
        if len(board) != 9:
            raise ValueError("Board must contain 9 elements.")
        self.board = board

    def is_goal(self):
        return self.board == self.GOAL_STATE

    def get_blank_index(self):
        return self.board.index(0)

    def get_neighbors(self):
        neighbors = []
        blank = self.get_blank_index()

        row = blank // 3
        col = blank % 3

        moves = {
            "UP": (row - 1, col),
            "DOWN": (row + 1, col),
            "LEFT": (row, col - 1),
            "RIGHT": (row, col + 1),
        }

        for move, (r, c) in moves.items():
            if 0 <= r < 3 and 0 <= c < 3:
                new_index = r * 3 + c
                new_board = list(self.board)
                new_board[blank], new_board[new_index] = (
                    new_board[new_index],
                    new_board[blank],
                )
                neighbors.append((move, PuzzleState(tuple(new_board))))

        return neighbors

    def __eq__(self, other):
        return isinstance(other, PuzzleState) and self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __str__(self):
        output = ""
        for i in range(0, 9, 3):
            row = self.board[i:i+3]
            output += "+---+---+---+\n"
            output += "|"
            for val in row:
                cell = " " if val == 0 else str(val)
                output += f" {cell} |"
            output += "\n"
        output += "+---+---+---+"
        return output