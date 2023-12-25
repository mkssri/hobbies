class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1Idx = {n:i for(i,n) in enumerate(nums1)}
        res = [-1]*len(nums1)

        stk = []

        for i in range(len(nums2)):

            curr_val = nums2[i]

            while(stk and curr_val>stk[-1]):

                val = stk.pop()
                idx = nums1Idx[val]
                res[idx] = curr_val
            
            if curr_val in nums1:
                stk.append(curr_val)
            
        return res