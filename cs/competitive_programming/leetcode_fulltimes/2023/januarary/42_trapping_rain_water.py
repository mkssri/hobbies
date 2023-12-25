from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        res = 0

        max_left = [0]*n
        max_right = [0]*n
        min_idx_lst = [0]*n

        max_val = height[0]
        for i in range(1,n):
            max_val = max(max_val, height[i-1])
            max_left[i] = max_val

        max_val = height[n-1]
        for x in range(n-2,-1,-1):
            max_val = max(max_val, height[x+1])
            max_right[x] = max_val

        for i in range(0,n):
            min_idx_lst[i] = min(max_left[i],max_right[i])
            diff = min_idx_lst[i]-height[i]

            if(diff>=0):
                min_idx_lst[i] = diff
            else:
                min_idx_lst[i] = 0
            res += min_idx_lst[i]
        
        return res


class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        res = 0
        if not height: return res
        
        l=0
        r=len(height)-1

        maxL,maxR = height[0],height[n-1]

        while(l<r):
        
            if(maxL<=maxR):
                l+=1
                diff=maxL-height[l]
                if diff>0: res+=diff
                maxL=max(maxL,height[l])
            else:
                r-=1
                diff=maxR-height[r]
                if diff>0: res+=diff
                maxR=max(maxR,height[r])
        
        return res