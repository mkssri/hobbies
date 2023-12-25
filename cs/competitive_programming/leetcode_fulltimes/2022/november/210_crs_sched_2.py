class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        store = { idx:[] for idx in range(numCourses) }
        visit_set, cycle_set = set(), set()
        res = []

        def dfs( crs ):
            
            if crs in visit_set:
                return True

            if crs in cycle_set:
                return False

            cycle_set.add( crs )

            for pre in store[crs]:
                if not dfs(pre): return False

            cycle_set.remove( crs )
            visit_set.add( crs )
            res.append( crs )

        
        
        for crs in range(numCourses):
            if not dfs(crs): return []

        return res

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        store=collections.defaultdict(list)
        res=[]
        visit=set()

        for x,y in prerequisites:
            store[x].append(y)
        
        def dfs(c,visit):
            if store[c]==[]:
                if c not in res:
                    res.append(c)
                return True
            if c in visit:
                return False

            visit.add(c)
            for nei in store[c]:
                if not dfs(nei,visit):return False
            
            visit.remove(c)
            if c not in res:
                res.append(c)
            store[c]=[]
            return True


        for i in range(numCourses):
            if not dfs(i,visit): return []
        return res
