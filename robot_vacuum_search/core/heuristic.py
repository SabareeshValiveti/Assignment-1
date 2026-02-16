import math
from typing import List, Tuple, FrozenSet

Position = Tuple[int, int]

def manhattan(a: Position, b: Position) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def mst_cost(points: List[Position]) -> int:
    if len(points) <= 1:
        return 0

    visited = [False]*len(points)
    dist = [math.inf]*len(points)
    dist[0] = 0
    total = 0

    for _ in range(len(points)):
        u = min(
            (i for i in range(len(points)) if not visited[i]),
            key=lambda i: dist[i]
        )
        visited[u] = True
        total += dist[u]

        for v in range(len(points)):
            if not visited[v]:
                d = manhattan(points[u], points[v])
                dist[v] = min(dist[v], d)

    return int(total)

def heuristic(position: Position,
              dirty_fs: FrozenSet[Position]) -> int:

    dirty = list(dirty_fs)
    if not dirty:
        return 0

    nearest = min(manhattan(position, d) for d in dirty)
    mst = mst_cost(dirty)
    clean_cost = len(dirty)

    return nearest + mst + clean_cost
