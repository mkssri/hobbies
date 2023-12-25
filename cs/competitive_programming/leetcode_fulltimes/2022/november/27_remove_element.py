class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        len_nums = len(nums)

        for idx in range(len_nums-1,-1,-1):
            ele = nums[idx]
            if ele == val:
                del nums[idx]
                
        return len(nums)