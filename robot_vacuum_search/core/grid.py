from typing import List, Set, Iterator, Tuple
from .state import State, Position

MOVE_DELTAS = {
    "MOVE_UP": (-1, 0),
    "MOVE_DOWN": (1, 0),
    "MOVE_LEFT": (0, -1),
    "MOVE_RIGHT": (0, 1),
}

class Grid:
    def __init__(self, grid_map: List[List[int]],
                 start: Position,
                 dirty: Set[Position]):

        self.grid = grid_map
        self.rows = len(grid_map)
        self.cols = len(grid_map[0])
        self.start = start
        self.dirty = set(dirty)

    def valid(self, pos: Position) -> bool:
        r, c = pos
        return (0 <= r < self.rows and
                0 <= c < self.cols and
                self.grid[r][c] == 0)

    def neighbors(self, state: State) -> Iterator[Tuple[State, str]]:
        (r, c), dirty_fs = state
        dirty = set(dirty_fs)

        for action, (dr, dc) in MOVE_DELTAS.items():
            nr, nc = r + dr, c + dc
            if self.valid((nr, nc)):
                yield ((nr, nc), dirty_fs), action

        if (r, c) in dirty:
            dirty.remove((r, c))
            yield ((r, c), frozenset(dirty)), "CLEAN"
