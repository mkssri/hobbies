#!/usr/bin/python3

from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = max(profit, prices[j]-prices[i])
        
        return profit

class Solution:
    def maxProfit(self, prices: List[int]):
        
        min_price = math.inf
        # min_price = prices[0]
        max_profit = 0

        for x in range(0, len(prices)):

            min_price = min(min_price, prices[x])
            max_profit = max(max_profit, prices[x]-min_price)
        
        return max_profit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit, min_stk = 0, []
        
        for i in range(len(prices)):
            if len(min_stk)==0:
                min_stk.append(prices[i])
            else:
                min_stk.append(min(min_stk[-1],prices[i]))
                profit = max(profit, prices[i]-min_stk[i])
        
        return profit
        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit, min_price = 0, math.inf
        
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i]-min_price)
        
        return profit



obj = Solution()
prices = [7,1,5,3,6,4]
out = obj.maxProfit(prices)

print(out)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit,min_price = 0, prices[0]
        idx, n = 0, len(prices)

        while(idx<n):
            min_price = min(min_price, prices[idx])
            profit = max(profit, (prices[idx]-min_price))
            idx += 1
        
        return profit
