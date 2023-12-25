class Solution:
    def maxArea(self, height: List[int]) -> int:

        #Brute Force
        res=0
        n=len(height)
        for i in range(n):
            for j in range(i+1,n):
                l=j-i
                b=min(height[i],height[j])
                res=max(res,l*b)
        return res

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L,R = 0,len(height)-1
        res=0
        while(L<=R):
            l=R-L
            b=min(height[L],height[R])
            res=max(res,l*b)
            if(height[L]<=height[R]):
                L+=1
            else:
                R-=1
        return res