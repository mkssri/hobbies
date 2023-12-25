class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums)-1

        while(l<= r):
            m = l + (r-l)//2
            mid_ele = nums[m]

            if(mid_ele==target):
                return m

            #Left
            if(mid_ele>=nums[l]):
                if(target>mid_ele or target<nums[l]):
                    l = m+1
                else:
                    r = m-1
            #Right
            else:
                if(target<mid_ele or target>nums[r]):
                    r = m-1
                else:
                    l = m+1

        return -1
