class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        res = [()]
        store=collections.defaultdict(list)

        for a,b in edges:
            store[a].append(b)
            store[b].append(a)

        
        def bfs(node, res):   
            q=collections.deque([node])
            while(len(q)>0):
                l=len(q)
                for _ in range(l):
                    ele=q.popleft()
                    res.add(ele)
                    for nei in store[ele]:
                        if nei not in res:
                            q.append(nei)
            return res
        
        res=set()
        cnt=0
        for i in range(n):
            if i in res:
                continue
            else:
                cnt+=1
                res=bfs(i,res)

        return cnt

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent=list(range(n))

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            p_x=find(x)
            p_y=find(y)

            if(p_x!=p_y):
                parent[p_y]=p_x
        
        for x,y in edges:
            union(x,y)

        store=collections.defaultdict(list)

        for idx,p in enumerate(parent):
            store[find(p)].append(idx)
        
        return len(store.keys())
