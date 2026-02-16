import matplotlib.pyplot as plt

def plot(results):

    algos = list(results.keys())
    nodes = [results[a]["nodes_expanded"] for a in algos]

    plt.figure()
    plt.bar(algos, nodes)
    plt.title("Nodes Expanded Comparison")
    plt.xlabel("Algorithm")
    plt.ylabel("Nodes Expanded")
    plt.show()
