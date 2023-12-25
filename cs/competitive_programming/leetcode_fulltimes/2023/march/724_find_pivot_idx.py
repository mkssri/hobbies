class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        t = 0

        for i in range(n):
            t += nums[i]

        i=0
        ls=0
        rs=t-ls
        while(i<n):
            rs -= nums[i]
            if(ls==rs):
                return i
            ls += nums[i]
            i += 1
        return -1

