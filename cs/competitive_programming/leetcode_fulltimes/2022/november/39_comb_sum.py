class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, cur, total):

            if total == target:
                res.append(cur.copy())
                return
            
            if i >=len(candidates) or total > target:
                return
            
            candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0, [], 0)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=list()
        l=len(candidates)

        def dfs(idx,cur,cur_total):
            
            # BASE Conditions
            if(cur_total>target or idx==l):
                return
            if(cur_total==target):
                res.append(cur.copy())
                return
            
            ele=candidates[idx]
            
            # include a index
            cur.append(ele)
            dfs(idx,cur,cur_total+ele)

            # ignore a index
            cur.pop()
            dfs(idx+1,cur,cur_total)



        
        dfs(0,[],0)
        return res
        
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=set()
        l=len(candidates)

        def dfs(idx,cur,cur_total):
            
            # BASE Conditions
            if(cur_total>target or idx==l):
                return
            if(cur_total==target):
                res.add(tuple(cur.copy()))
            
            ele=candidates[idx]
            
            # include a index
            cur.append(ele)
            dfs(idx,cur,cur_total+ele)

            # ignore a index
            cur.pop()
            dfs(idx+1,cur,cur_total)

