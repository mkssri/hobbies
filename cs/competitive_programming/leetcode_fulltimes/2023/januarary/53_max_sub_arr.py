class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        # even and odd subarrays
        res=nums[0]
        n=len(nums)

        def helper(l,r,tmp,res):
            while(l>=0 and r<n):
                if(l==r):
                    tmp+=nums[l]
                else:
                    tmp+=nums[l]
                    tmp+=nums[r]
                res=max(res,tmp)
                l-=1
                r+=1
            return res


        for i in range(n):
            tmp=0
            l,r=i,i
            res1=helper(i,i,tmp,res)
            l,r=i,i+1
            res2=helper(i,i+1,tmp,res)
            res=max(res1,res2)
        
        return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res,curr_sum=nums[0],0

        for n in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=n
            res=max(res, curr_sum)
        return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res, cur_sum = nums[0], 0

        for n in nums:

            if cur_sum < 0:
                cur_sum = 0
            cur_sum += n
            res = max(res, cur_sum)
        return res
