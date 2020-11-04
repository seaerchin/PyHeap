# PyHeap
PyHeap is an attempt to write a max heap in python that accepts lambda functions for comparison. What this does is that now, the heap can be sorted according to how the consumer (you) wants it to be sorted.

The heap class also uses a list as its underlying data structure so it's easy to obtain items back from the underlying heap.

# Why this?
the original heapq algorithm as given in the python library doesn't allow for custom comparison; instead, consumers have to alter their data definition to fit the module. doing so leads to unclear code; hence, this attempts to fix a pain point there.
