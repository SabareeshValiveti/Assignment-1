import time
from core.grid import Grid
from algorithms import dfs, astar, idastar
from tests.test_cases import get_tests
from utils.performance_plot import plot

def run_all():

    tests = get_tests()

    for test in tests:
        print(f"\n===== {test['name']} =====")

        grid = Grid(test["grid"],
                    test["start"],
                    test["dirty"])

        results = {}

        for name, algo in [
            ("DFS", dfs.run),
            ("A*", astar.run),
            ("IDA*", idastar.run)
        ]:
            start = time.time()
            res = algo(grid)
            res["time"] = time.time() - start
            results[name] = res

            print(name, res)

        plot(results)

if __name__ == "__main__":
    run_all()
