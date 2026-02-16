import math
from typing import Dict, Any
from core.priority_queue import PriorityQueue
from core.heuristic import heuristic
from core.state import State
from core.grid import Grid

def run(grid: Grid) -> Dict[str, Any]:

    start: State = (grid.start, frozenset(grid.dirty))

    open_set = PriorityQueue()
    g_score = {start: 0}
    parent = {}

    open_set.push(start, heuristic(*start))

    nodes_expanded = 0
    max_frontier = 1

    while True:
        current, _ = open_set.pop()
        nodes_expanded += 1
        max_frontier = max(max_frontier, len(open_set))

        pos, dirty = current
        if not dirty:
            return {
                "cost": g_score[current],
                "nodes_expanded": nodes_expanded,
                "max_frontier": max_frontier
            }

        for nxt, action in grid.neighbors(current):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(nxt, math.inf):
                g_score[nxt] = tentative_g
                f = tentative_g + heuristic(*nxt)
                open_set.push(nxt, f)
