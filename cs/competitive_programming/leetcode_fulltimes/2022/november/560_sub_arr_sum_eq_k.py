"""
TLE Lol! :)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        res = 0
        for i in range(len(nums)):
            cnt = nums[i]
            if cnt == k:
                res += 1
            for j in range(i+1,len(nums)):
                cnt += nums[j]
                if cnt == k:
                    res += 1

        return res
    
"""
Good Solution! :)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        store, res ={0:1}, 0

        curr_sum = 0
        for num in nums:
            curr_sum += num
            
            if(curr_sum-k) in store:
                res += store[curr_sum-k]

            store[curr_sum] = store.get(curr_sum,0)+1
        
        return res