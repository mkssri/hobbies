class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        res = 0
        prev1, prev2 = 1, 0
        
        for _ in range(2, n+1):

            res = prev2 + prev1
            prev2 = prev1
            prev1 = res

        return res
    
class SolutionRecurvsive:
    def fib_recursive(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        return self.fib_recursive(n-1)+self.fib_recursive(n-2)