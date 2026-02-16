import heapq

REMOVED = "<removed>"

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.counter = 0

    def push(self, item, priority):
        if item in self.entry_finder:
            self.remove(item)

        entry = [priority, self.counter, item]
        self.counter += 1
        self.entry_finder[item] = entry
        heapq.heappush(self.heap, entry)

    def remove(self, item):
        entry = self.entry_finder.pop(item)
        entry[-1] = REMOVED

    def pop(self):
        while self.heap:
            priority, _, item = heapq.heappop(self.heap)
            if item is not REMOVED:
                del self.entry_finder[item]
                return item, priority
        raise KeyError("empty queue")

    def __len__(self):
        return len(self.entry_finder)
