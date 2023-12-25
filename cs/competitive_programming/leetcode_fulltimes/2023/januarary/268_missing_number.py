class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        for num in range(n+1):
            if num in nums:
                continue
            else:
                return num
            
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        set1=set(nums)

        for num in range(n+1):
            if num in set1:
                continue
            else:
                return num
            
            
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        set1=set(nums)
        cmp = list(range(0,n+1))
        i = 0

        while(i<=n):
            if cmp[i] not in set1:
                return cmp[i]
            i+=1
            
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        i = 0

        while(i+1<n):
            if nums[i+1]-nums[i] > 1:
                return nums[i]+1
            i += 1
        if nums[-1]==n:
            return 0
        else:
            return nums[-1]+1
            
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        s = (n*(n+1))//2
        c_s = 0

        for x in nums:
            c_s += x

        return s-c_s

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)

        for i in range(n):
            if i == nums[i]:
                continue
            else:
                return i
        return n
