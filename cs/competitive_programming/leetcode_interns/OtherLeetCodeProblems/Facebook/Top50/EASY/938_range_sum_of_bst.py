#!/usr/bin/python3

from typing import List, Optional

# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        self.out = 0
        
        self.dfs(root)
        
        print("out - {}".format(self.out))
        
        return self.out
    
    
    def dfs(self, node):
        
        if node:
            self.dfs(node.left)
            
            if node.val >= self.low and node.val <= self.high:
                self.out += node.val
            
            self.dfs(node.right)

class Solution1:
    
    
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.low = low
        self.high = high
        out = 0
        out = self.dfs(root, out)
    
        return out
    
    
    def dfs(self, node, out):
        
        if node:
            out = self.dfs(node.left, out)
            
            if node.val >= self.low and node.val <= self.high:
                out += node.val
            
            out = self.dfs(node.right, out)
            
        return out 
"""
Time Complexity - O(n^2)
Space Complexity - O(n)
"""
        
# Leetcode recursive solution
class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(node):
            
            if node:
                
                if node.val >= low and node.val <= high:
                    self.result += node.val
                    
                if low < node.val:
                    dfs(node.left)
                
                if node.val < high:
                    dfs(node.right)
                    
            
            
            
        self.result = 0
        dfs(root)
        return self.result

# Leetcode iterative solution
"""
Time Complexity - O(n)
Space Complexity - O(n)
"""


class Solution3:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        ans = 0
        stack = [root]
        
        
        while len(stack) > 0:
            
            node = stack.pop()
            
            if node:
            
                if node.val >= low and node.val <= high:
                    ans += node.val

                if node.val > low:
                        stack.append(node.left)

                if node.val < high:
                        stack.append(node.right)
        
        return ans
        