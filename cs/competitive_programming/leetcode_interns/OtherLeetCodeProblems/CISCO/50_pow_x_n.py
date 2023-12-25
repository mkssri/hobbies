#!/usr/bin/python3

#BRUTE FORCE METHOD
"""
Time Complexity - O(N) 
Space Complexity - O(1)
""" 
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n < 0:
            x = 1/x
            n = -n
        
        ans = 1
        
        for i in range(0,n):
            ans = ans*x
        
        return ans    

# Fast Power Algorithm Recursive
"""
Time Complexity - O(logN) 
Space Complexity - O(logN)
""" 
class Solution1(object):
    
    def fastPow(self,x,n):
        
        #BASE CASE
        if n == 0:
            return 1
        
        half = self.fastPow(x, n//2)
        
        if(n%2 == 0):
            return half * half
        else:
            return half * half * x
        
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        return self.fastPow(x, n)
    
    
# Fast Power Algorithm Iterative
"""
Time Complexity - O(logN) 
Space Complexity - O(1)
""" 
class Solution2(object):
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
            
        ans = 1
        current_product = x
        return self.fastPow(x, n)




if __name__ == "__main__":
    obj = Solution()
    x,n = 2, 10
    out = obj.myPow()