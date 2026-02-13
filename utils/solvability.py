# utils/solvability.py

def count_inversions(board: tuple) -> int:
    """
    Counts number of inversions in board (ignoring 0).
    """
    arr = [x for x in board if x != 0]
    inversions = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1

    return inversions


def is_solvable(board: tuple) -> bool:
    """
    For 3x3 puzzle:
    Solvable if inversion count is even.
    """
    inversions = count_inversions(board)
    return inversions % 2 == 0