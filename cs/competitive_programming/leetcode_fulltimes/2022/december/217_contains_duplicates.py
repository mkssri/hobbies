from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not(len(nums)==len(set(nums))
