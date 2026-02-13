# core/node.py

class Node:
    def __init__(self, state, parent=None, move=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g  # path cost
        self.h = h  # heuristic
        self.f = g + h
        self.depth = 0 if parent is None else parent.depth + 1

    def reconstruct_path(self):
        """
        Returns list of nodes from root to current node.
        """
        path = []
        current = self
        while current:
            path.append(current)
            current = current.parent
        return list(reversed(path))

    def __lt__(self, other):
        """
        Required for priority queue (heapq).
        Compares based on f value.
        """
        return self.f < other.f

    def __repr__(self):
        return f"Node(g={self.g}, h={self.h}, f={self.f}, depth={self.depth})"