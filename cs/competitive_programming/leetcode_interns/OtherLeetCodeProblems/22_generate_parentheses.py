#!/usr/bin/python3

# Link - https://leetcode.com/problems/generate-parentheses/

# Solution - https://www.youtube.com/watch?v=s9fokUqJ76A


from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Only add open paranthesis if open < n
        Only add closed paranthesis if closed < open
        Valid IIF open == closed == n (only add stopping!!)
        """
        
        # which is going to hold the paranthsis
        stack = [] 
        
        # Which has list of valid paranthesis
        res = []
        
        def backtrack(openN, closedN):
            
            print("openN {} and cosedN {}".format(openN, closedN))
            
            # BASE CASE
            if openN == closedN == n:
                res.append("".join(stack))
                return
        
        
            # Add open paranthesis if openN < n
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # Add closed paranthesis if closedN < openN
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()
            
        backtrack(0, 0)        
        return res









if __name__ == "__main__":
    
    n = 3
    
    obj = Solution()
    out = obj.generateParenthesis(n)
    print(out)