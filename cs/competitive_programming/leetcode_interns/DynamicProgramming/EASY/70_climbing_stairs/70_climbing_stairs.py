#!/usr/bin/python3

# Link - https://leetcode.com/problems/climbing-stairs/


import math

class Solution(object):
    
    """
    TIME COMPLEXITY - O(N)
    SPACE COMPLEXITY - O(1)
    """
    def climbStairs(self, n):
        """
        :type n: int (1 <= n <= 45)
        :rtype: int
        """
        
        if n == 1:
            return 1
        
        # Any number can be generated using 1
        count = 1
        
        # n is even
        if n%2 == 0:            
            max_num_of_1_s = n
            max_num_of_2_s = n/2
        # n is odd    
        else: 
            max_num_of_1_s = n
            max_num_of_2_s = (n-1)/2
            
        while max_num_of_2_s > 0:

            num_of_twos = max_num_of_2_s
            num_of_ones = n - 2*num_of_twos

            count += math.factorial(num_of_twos+num_of_ones)/(math.factorial(num_of_twos)*math.factorial(num_of_ones))

            max_num_of_2_s -= 1

        return count
                    

        