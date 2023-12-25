class Solution:
    def rob(self, nums: List[int]) -> int:
    
        def helper(nums):
            rob1,rob2 = 0,0
            for n in nums:
                tmp=max(rob1+n,rob2)
                rob1=rob2
                rob2=tmp
            return rob2

        if len(nums)==1:
            return nums[0]
        
        nums1=nums[1:]
        nums2=nums[0:len(nums)-1]

        return max(helper(nums1), helper(nums2))