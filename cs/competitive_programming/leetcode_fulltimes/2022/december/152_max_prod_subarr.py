import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res=-math.inf

        def helper(nums, l, r, res):
            cnt=0
            while(l>=0 and r<=len(nums)-1):
                if cnt==0:
                    if l==r:
                        p=nums[l]
                    else:
                        p=nums[l]*nums[r]
                else:
                    p=p*nums[l]*nums[r]
                res=max(res,p)
                r+=1
                l-=1
                cnt+=1
            return res


        for i in range(len(nums)):
            #odd
            res=helper(nums,i,i,res)
            #even
            res=helper(nums,i,i+1,res)

        return res
    
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curr_min, curr_max = 1, 1
        res=max(nums)

        for n in nums:
            if n==0:
                curr_min, curr_max = 1, 1
            tmp = curr_max
            curr_max = max(n*curr_max, n*curr_min, n)
            curr_min = min(tmp*n, n*curr_min, n)
            res=max(res,curr_max)
        return res