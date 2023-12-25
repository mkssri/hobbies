
import collections

class Solution:
    
    def helper(self, n, edges):
        
        store=collections.defaultdict(list)
        for edge in edges:
            store[edge[0]].append(edge[1])
        global_set=set()
          
        # lst=[3,4,0,1,2]
        for node in range(n):
        # for node in lst:
            if(len(global_set)==n):
                return True
            if(node in global_set):
                continue
                
            local_set=set()
            q=collections.deque([node])
            
            while q:
                l=len(q)
                for _ in range(l):
                    ele=q.popleft()
                    global_set.add(ele)
                    if ele in local_set:
                        return False
                    local_set.add(ele)
                    for nei in store[ele]:
                        q.append(nei)
        
        return len(global_set)==n
   

edges=[[0,1],[1,2],[1,4],[2,3],[4,0]]
n=5
obj=Solution()
res=obj.helper(n,edges)
print(res)

