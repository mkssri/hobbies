class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                profit = max(profit, prices[j]-prices[i])
        
        return profit

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