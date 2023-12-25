class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def dfs(i,sub):
            if i == len(nums):
                res.append(sub.copy())
                return
            
            # include
            sub.append(nums[i])
            dfs(i+1,sub)
            sub.pop()

            # not include
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,sub)


        dfs(0,[])
        return res
    
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = set()

        sub=[]
        def dfs(i):
            if i == len(nums):
                tmp = sub.copy()
                tmp.sort()
                tmp=tuple(tmp)
                res.add(tmp)
                return
            
            # include
            sub.append(nums[i])
            dfs(i+1)

            # not include
            sub.pop()
            dfs(i+1)


        dfs(0)
        return list(res)