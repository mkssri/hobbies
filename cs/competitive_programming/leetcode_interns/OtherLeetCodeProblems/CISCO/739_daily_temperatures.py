#!/usr/bin/python3

# Link - https://leetcode.com/problems/daily-temperatures/
# Youtube - https://www.youtube.com/watch?v=cTBiBSnjO3c&t=605s


import math
from typing import List

"""
TIME COMPLEXITY - O(N^2)
SPACE COMPLEXITY - O(N)
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        out_lst = []
        len_temperatures = len(temperatures)        
        for x in range(len_temperatures):
             
            next_warmer_day = 0
            
            for y in range(x, len_temperatures):
                
                if temperatures[y] > temperatures[x]:
                    next_warmer_day = y-x
                    break
                
            out_lst.append(next_warmer_day)
                
                
            
        return out_lst

    """
    TIME COMPLEXITY - O(N)
    SPACE COMPLEXITY - O(N)
    """ 

    def dailyTemperaturesv1(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        res = [0]*len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i,t in enumerate(temperatures):
            
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
                
            stack.append([t,i])
        
        return res
        


    


if __name__ == "__main__":
    
    obj = Solution()
    
    temperatures = [73,74,75,71,69,72,76,73]
    out = obj.dailyTemperaturesv1(temperatures)
    print(out)
    
    temperatures = [30,40,50,60]
    out = obj.dailyTemperaturesv1(temperatures)
    print(out)


    temperatures = [30,60,90]
    out = obj.dailyTemperaturesv1(temperatures)
    print(out)

