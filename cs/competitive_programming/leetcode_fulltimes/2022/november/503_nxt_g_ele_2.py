class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        

        n = len(nums)
        stk = []
        res = [-1]*n


        for idx in range(0,2*n):
            
            curr_ele = nums[idx%n]
            while( stk!=[] and nums[stk[-1]]<curr_ele ):
                res[stk.pop()]=curr_ele
            if(idx<n):
                stk.append(idx)
                
        return res