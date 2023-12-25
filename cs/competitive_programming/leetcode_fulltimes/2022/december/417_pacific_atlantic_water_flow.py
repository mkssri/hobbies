class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        R=len(heights)
        C=len(heights[R-1])
        p,a=[],[]
        vp,va=set(),set()

        #starting
        for r in range(R):
            p.append((r,0))
            a.append((r,C-1))

        for c in range(C):
            p.append((0,c))
            a.append((R-1,c))

        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(r,c,visited):
            visited.add((r,c))
            for dr,dc in dirs:
                nr=r+dr
                nc=c+dc
                if( (nr>=0 and nr<R) and (nc>=0 and nc<C) and (heights[r][c]<=heights[nr][nc]) and (nr,nc) not in visited ):
                    dfs(nr,nc,visited)
        
        for r,c in p: dfs(r,c,vp)
        for r,c in a: dfs(r,c,va)

        return vp.intersection(va)