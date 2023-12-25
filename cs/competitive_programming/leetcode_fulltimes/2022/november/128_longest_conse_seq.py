class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        longest_str = 0

        for num in nums:

            # Check if num is start of the sequence
            if(num-1) not in nums_set:
                length = 0
                while(num+length) in nums_set:
                    length += 1
        
                longest_str = max(longest_str, length)

        return longest_str

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        cnt = 0

        for num in nums:
            if num-1 not in nums_set:
                l=0
                while((num+l) in nums_set):
                    l+=1
                cnt=max(cnt,l)
        return cnt
