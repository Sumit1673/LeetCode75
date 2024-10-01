from typing import *
def zigzag_iter(a: List[int], b: List[int]) -> List[int]:


    min_len = min(len(a), len(b))
    res = []
    for ai, bi in zip(a,b):
        res.append(ai)
        res.append(bi)

    if len(a)< len(b):
        return res + b[min_len:]
    else:
        return res + a[min_len :]
    

#zigzag_iter([1,2], [3,4,5,6])
zigzag_iter([], [1])

class ZigZagIterator:
    def __init__(self, *args) -> None:
        self.v1= args[0]
        self.v2 = args[1]
        self.n =  sum(map(len, [self.v1, self.v2]))
        self.i, self.j = 0,0


    def _len_(self):
        return self.n
        
    def next(self):
        if not self.hasnext: return False

        if self.i >= len(self.v1):
            self.j += 1
            return self.v2[self.j - 1]

        if self.j >= len(self.v2):
            self.i += 1
            return self.v1[self.i - 1]
        if self.i <= self.j:
            self.i+=1
            return self.v1[self.i-1]
        else:
            self.j += 1
            return self.v2[self.j-1]

    def hasnext(self):
        if self.i >= len(self.v1) and self.j >= len(self.v2):
            return False
        return True

import heapq

class ZigzagIteratorK:
    def __init__(self, vectors: List[List[int]]):
        self.vectors = vectors
        self.pq = []
        for i, vec in enumerate(vectors):
            if vec:
                heapq.heappush(self.pq, (0, i, 0))  # (defines the position in heap, index of vector, index of element in vector)
        self.hasNext = bool(self.pq)

    def next(self) -> int:
        if not self.hasNext:
            return -1
        _, i, j = heapq.heappop(self.pq)
        if j + 1 < len(self.vectors[i]): # if a vector is done iterating dont add to the heap
            # this helps in maintaing the min heap property
            # we initialized our heap with 0,0,0 -> 0,1,0 -> 0,2,0 after next 1,0,1, 1,1,1, 1,2,1 
            heapq.heappush(self.pq, (j + 1, i, j + 1)) 

        self.hasNext = bool(self.pq)
        return self.vectors[i][j]
    

zigzag2 = ZigzagIteratorK([[1,2,11,12,13], [3,4,5,6], [7,8,9]])
while zigzag2.hasNext:
    print(zigzag2.next())

