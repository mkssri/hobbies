#!/usr/bin/python3

# Link - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""
Complexity Analysis

Time complexity : O(m). A total of m nodes need to be traversed. 
Here, m represents the minimum number of nodes from the two given trees.

Space complexity : O(m). The depth of the recursion tree can go upto mm in the case of a skewed tree. 
In average case, depth will be O(logm).
"""        

class Solution1:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
        if(root1 == None):
            return root2
        if(root2 == None):
            return root1

        root1.val += root2.val

        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

        
# class Solution2:
#     def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        
