from typing import Dict, Any
from core.state import State
from core.grid import Grid

def run(grid: Grid) -> Dict[str, Any]:

    start: State = (grid.start, frozenset(grid.dirty))

    stack = [(start, [], 0)]
    explored = set()

    nodes_expanded = 0
    max_frontier = 1

    while stack:
        max_frontier = max(max_frontier, len(stack))
        state, path, cost = stack.pop()

        if state in explored:
            continue

        explored.add(state)
        nodes_expanded += 1

        _, dirty = state
        if not dirty:
            return {
                "solution": path,
                "cost": cost,
                "nodes_expanded": nodes_expanded,
                "max_frontier": max_frontier
            }

        for nxt, action in reversed(list(grid.neighbors(state))):
            if nxt not in explored:
                stack.append((nxt, path+[action], cost+1))

    return None
