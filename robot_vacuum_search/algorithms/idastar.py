from typing import Dict, Any
from core.heuristic import heuristic
from core.grid import Grid
from core.state import State
import math

def run(grid: Grid) -> Dict[str, Any]:

    start: State = (grid.start, frozenset(grid.dirty))
    bound = heuristic(*start)

    iterations = 0
    nodes_expanded = 0

    def dfs(state, g, bound, visited):
        nonlocal nodes_expanded
        nodes_expanded += 1

        f = g + heuristic(*state)
        if f > bound:
            return None, f

        if not state[1]:
            return True, f

        min_over = math.inf

        for nxt, _ in grid.neighbors(state):
            if nxt in visited:
                continue
            visited.add(nxt)
            res, t = dfs(nxt, g+1, bound, visited)
            if res:
                return True, t
            min_over = min(min_over, t)
            visited.remove(nxt)

        return None, min_over

    while True:
        iterations += 1
        visited = {start}
        result, new_bound = dfs(start, 0, bound, visited)

        if result:
            return {
                "cost": bound,
                "nodes_expanded": nodes_expanded,
                "iterations": iterations
            }

        bound = new_bound
