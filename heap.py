from math import inf

class Heap(): 
    def __init__(self, ls = [], f = lambda x, y: x > y):
        """ 
        ls is a list which is not assumed to be a heap; f is the comparison function which is used to construct the heap.
        of note, we assume the following invariants about the heap: left(i) returns the left child of heap rooted at i; right(i) returns the right child of heap rooted at i.
        """ 
        self.ls = self.buildMaxHeap(ls)
        self.f = f
    
    def maxHeapify(self, ls, i):
        """ maxHeapify fixes the max heap at i. in particular, it assumes that left(i) and right(i) are both heaps but does not assume that ls[i] itself is a heap """ 
        l, r = self.left(i), self.right(i)
        # first, assume that the heap invariant holds 
        largest = i
        if l <= len(ls) and self.f(ls[l], ls[i]):
            largest = l
        if r <= len(ls) and self.f(ls[r], ls[i]):
            largest = r
        # invariant violated -> we need to fix this
        if largest != i: 
            ls[largest], ls[i] = ls[i], ls[largest]
            ls = self.maxHeapify(ls, largest)
        return ls

    def left(self, i): 
        # NOTE: caller checks for indexError
        return 2 * i
    
    def right(self, i):
        # NOTE: caller checks for indexError
        return 2 * i + 1

    def buildMaxHeap(self, arr): 
        for i in range(len(arr) // 2, 0, -1):
            self.maxHeapify(arr, i)
        return arr