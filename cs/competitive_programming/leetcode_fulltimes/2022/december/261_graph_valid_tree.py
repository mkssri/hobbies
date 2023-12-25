import collections
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if n>1 and len(edges)==0:
            return False
        
        if n==1 and len(edges)==0:
            return True

        store=collections.defaultdict(list)
        for a,b in edges:
            store[a].append(b)
            store[b].append(a)

        st=edges[0][0]

        q=collections.deque([st])
        visit_set=set() 
        visit_edge=set()
        while(len(q)>0):
            l=len(q)
            for _ in range(l):
                ele=q.popleft()
                if ele in visit_set:
                    return False
                visit_set.add(ele)
                for nei in store[ele]:
                    if str(ele)+'-'+str(nei) not in visit_edge and str(nei)+'-'+str(ele) not in visit_edge:
                        q.append(nei)
                        visit_edge.add(str(ele)+'-'+str(nei))

        return len(visit_set)==n