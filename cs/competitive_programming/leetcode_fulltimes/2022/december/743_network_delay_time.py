import collections
from typing import List
from heapq import heappush, heappop

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        store=collections.defaultdict(list)

        for n1,n2,w in times:
            store[n1].append((w,n2))

        visit_set=set()
        min_heap=[(0,k)]
        t = 0

        while min_heap:
            w1,n1 = heappop(min_heap)
            if n1 in visit_set:
                continue
            visit_set.add(n1)
            t=max(t,w1)
            for w2,n2 in store[n1]:
                if n2 not in visit_set:
                    heappush(min_heap, (w1+w2,n2))
        
        return t if len(visit_set)==n else -1