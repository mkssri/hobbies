class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Cool solution: Do BFS from all the Gates! Wow :)

        R=len(rooms)
        C=len(rooms[R-1])

        visit=set()
        q=collections.deque([])

        for r in range(R):
            for c in range(C):
                if rooms[r][c]==0:
                    visit.add((r,c))
                    q.append((r,c))

        def addNext(r,c):
            if(r<0 or c<0 or r==R or c==C or ((r,c) in visit) or rooms[r][c]==-1):
                return
            visit.add((r,c))
            q.append((r,c))


        #BFS
        dist=0
        while(q):
            l=len(q)
            for _ in range(l):
                r,c=q.popleft()
                rooms[r][c]=dist
                addNext(r+1,c)
                addNext(r-1,c)
                addNext(r,c+1)
                addNext(r,c-1)
            dist+=1