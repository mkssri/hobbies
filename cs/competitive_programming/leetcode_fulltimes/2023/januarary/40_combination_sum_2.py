from typing import List

# Time Limit Exceeded (TLE)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        l=len(candidates)
        res=[]

        def helper(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i==l:
                return
            
            # include index
            cur.append(candidates[i])
            helper(i+1, cur, total+candidates[i])

            cur.pop()
            while(i+1<l and candidates[i+1]==candidates[i]):
                i += 1

            # discard index
            helper(i+1, cur, total)


        # i, cur_lst, total
        helper(0, [], 0)
        return res
    
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        l=len(candidates)
        res=[]

        def helper(i, cur, total):
            if total == target:
                res.append(cur.copy())
            if total>=target or i==l:
                return
            
            # include index
            cur.append(candidates[i])
            helper(i+1, cur, total+candidates[i])

            cur.pop()
            while(i+1<l and candidates[i+1]==candidates[i]):
                i += 1

            # discard index
            helper(i+1, cur, total)


        # i, cur_lst, total
        helper(0, [], 0)
        return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        res = []
        l=len(candidates)

        def dfs(pos, cur, target ):
            if target==0:
                res.append(cur.copy())
            if target<=0:
                return
            prev=-1
            for i in range(pos,l):
                if candidates[i]==prev:
                    continue
                cur.append(candidates[i])
                dfs(i+1, cur, target-candidates[i])
                cur.pop()

                prev=candidates[i]
        
        dfs(0,[], target)
        return res