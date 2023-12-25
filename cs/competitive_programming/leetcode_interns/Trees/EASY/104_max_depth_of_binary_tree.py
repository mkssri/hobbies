#!/usr/bin/python3

# Link - https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        else:
            left_path = self.maxDepth(root.left)
            right_path = self.maxDepth(root.right)
            
            
            return max(left_path, right_path) + 1