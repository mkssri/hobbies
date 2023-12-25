class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        start, end = 0, 0

        while( end < len(nums) ):

            if nums[end] == 0:
                k -= 1
            
            if(k<0):

                if nums[start]==0:
                    k += 1
                
                start += 1
            
            end += 1
        
        return end - start