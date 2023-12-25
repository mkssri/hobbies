class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        store = collections.defaultdict(list)
        visit_set = set()        

        for ele in prerequisites:
            c, p = ele[0], ele[1]
            store[c].append(p)


        def dfs(c):
            
            if c in visit_set:
                return False
            
            if store[c] == []:
                return True

            visit_set.add(c)
            
            # Running DFS on prequisites
            for p in store[c]:
                if not dfs(p): return False

            visit_set.remove(c)
            store[c] = []
            return True


        # Do DFS on all courses
        for c in range(numCourses):
            if not dfs(c): return False

        return True

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        store=collections.defaultdict(list)

        for x,y in prerequisites:
            store[x].append(y)
        
        def dfs(c,visit):
            if store[c]==[]:
                return True
            if c in visit:
                return False

            visit.add(c)
            for nei in store[c]:
                if not dfs(nei,visit): return False
            
            visit.remove(c)
            store[c]=[]
            return True

                
        visit=set()
        for i in range(numCourses):
            if not dfs(i,visit):return False
        
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        store=collections.defaultdict(list)

        for ele in prerequisites:
            store[ele[0]].append(ele[1])

        cycle_set=set()

        def dfs(c):
            
            if store[c]==[]:
                return True
            if c in cycle_set:
                return False

            cycle_set.add(c)

            for p in store[c]:
                if not dfs(p): return False
            
            cycle_set.remove(c)
            store[c]=[]
            
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

