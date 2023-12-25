class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
        Time Complexity: O(2^N)
        Space Complexity: O(2^N)
        """

        res=[[]]

        for n in nums:
            tmp=[]
            for lst in res:
                tmp += [lst+[n]]
            res += tmp
        return res
    
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        subset=[]
        def dfs(i):
            if i==len(nums):
                res.append(subset.copy())
                return
            
            # to include an element
            subset.append(nums[i])
            dfs(i+1)

            # to not include an element
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res