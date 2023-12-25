#!/usr/bin/python3

# Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List
import math

# Brute Force Method (time limit extended)
"""
Time Complexity - O(N^2)
Space Complexity - O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        for i in range(len(prices)):
            
            for j in range(i+1, len(prices)):
                
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        
        return max_profit

# (time limit extended)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        
        for x in range(len(prices)):
            
            buy_price = prices[x]
            max_sell_price = self.maxSellPrice(prices[x+1:len(prices)])
            profit = max_sell_price - buy_price
            max_profit = max(profit, max_profit)            
        return max_profit
    
    def maxSellPrice(self, prices):
        
        if len(prices) != 0:
            return max(prices)
        else:
            return 0

# One Passmethod (worked)

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        
            max_profit = 0
            min_price = math.inf
            
            for i in range(len(prices)):
                
                # MINIMUM Price 
                min_price = min(min_price, prices[i])
                
                # Checking for the peak aft the minimum price
                max_profit = max(max_profit, prices[i]-min_price)
                                    
            return max_profit
        
if __name__ == "__main__":
    
    obj = Solution()
    
    prices = [7,1,5,3,6,4]
    out = obj.maxProfit(prices)
    print(out)
    
    prices = [7,6,4,3,1]
    out = obj.maxProfit(prices)
    print(out)

    obj1 = Solution1()
    
    prices = [7,1,5,3,6,4]
    out = obj1.maxProfit(prices)
    print(out)
    
    prices = [7,6,4,3,1]
    out = obj1.maxProfit(prices)
    print(out)

    obj2 = Solution1()
    
    prices = [7,1,5,3,6,4]
    out = obj2.maxProfit(prices)
    print(out)
    
    prices = [7,6,4,3,1]
    out = obj2.maxProfit(prices)
    print(out)