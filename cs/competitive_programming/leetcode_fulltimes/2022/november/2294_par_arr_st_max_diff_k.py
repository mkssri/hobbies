class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums.sort()
        res = 0
        while nums:
            small_ele = nums.pop(0)
            while nums and small_ele <= nums[0] and nums[0]-small_ele <= k:
                nums.pop(0)
            res += 1

        return res