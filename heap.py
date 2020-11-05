from math import inf

class Heap(): 
    def __init__(self, ls = [], f = lambda x, y: x > y):
        """ 
        ls is a list which is not assumed to be a heap; f is the comparison function which is used to construct the heap.
        of note, we assume the following invariants about the heap: left(i) returns the left child of heap rooted at i; right(i) returns the right child of heap rooted at i.
        """ 
        self.ls = ls
        self.f = f
    
    def maxHeapify(self, i):
        """ maxHeapify fixes the max heap at i. in particular, it assumes that left(i) and right(i) are both heaps but does not assume that ls[i] itself is a heap """ 
        l, r = self.left(i), self.right(i)
        # first, assume that the heap invariant holds 
        largest = i
        if l < len(self.ls) and self.f(self.ls[l], self.ls[largest]):
            largest = l
        if r < len(self.ls) and self.f(self.ls[r], self.ls[largest]):
            largest = r
        # invariant violated -> we need to fix this
        if largest != i: 
            self.ls[largest], self.ls[i] = self.ls[i], self.ls[largest]
            self.maxHeapify(largest)

    def left(self, i): 
        return 2 * (i + 1) - 1
    
    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i) // 2

    def buildMaxHeap(self): 
        for i in range(len(self.ls) // 2, -1, -1):
            self.maxHeapify(i)

    def getList(self):
        return self.ls

    def getMax(self):
        """ gets the max from the heap. this can throw if the heap itself is empty """ 
        res = self.ls.pop(0)
        self.maxHeapify(0)
        return res

    def isEmpty(self):
        return len(self.ls) == 0

    def __str__(self): 
        return str(self.getList())
    
    def push(self, item): 
        self.ls.append(item)
        cur = len(self.ls) - 1 
        p = self.parent
        while cur >= 0 and self.ls[p(cur)] < self.ls[cur]: 
            self.ls[p(cur)], self.ls[cur] = self.ls[cur], self.ls[p(cur)]
            cur = p(cur)

if __name__ == '__main__':
    heap = Heap()
    x = [3, 2, 5, 6, 10, 7, 1]
    for i in x: 
        heap.push(i)
    heap.push(8)
    print(heap)