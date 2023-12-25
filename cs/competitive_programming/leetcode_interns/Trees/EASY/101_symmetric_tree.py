#!/usr/bin/python3

# Link - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 

# APPROACH 1 - RECURSIVE       
        
"""
Time complexity : O(n)
Space complexity : O(n)
"""
        
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.isMirror(root, root)
    
    def isMirror(self, t1, t2):
        
        if (t1 == None) and (t2 == None):
            return True
        if (t1 == None) or (t2 == None):
            return False
        
        return((t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right))
    
# APPROACH 2 - ITERATIVE

# TODO 
"""
did not follow much
"""       
