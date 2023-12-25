#!/usr/bin/python3

# Link - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Link - GOG - https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right




# RECURSION

"""
TIME COMPLEXITY - O(n). The time complexity is O(n) because the recursive function is T(n) = 2.  T(n/2)+1
SPACE COMPLEXITY - The worst case space required is O(n), and in the average case it's O(logn) where n is number of nodes.
"""


class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]: 
        
        res = []
        self.helper(root, res)
        return  res
    
    def helper(self, root, res):
        
        # INORDER TRAVERSAL -> Left, Root and Right
        
        if root != None:
        
            self.inorderTraversal(root.left, res)
            res.append(root.val)
            self.inorderTraversal(root.right, res)
    

# Approach 2: Iterating method using Stack


            
            
# TODO
"""
REFER to Lettcode Approach2 to implement using iterative method (Using Stack)
Complexity Analysis-
Time complexity : O(n)
Space complexity : O(n)
"""

class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:        
        
    
        res = []
        stack = []
        
        curr = root
        
        while (curr != None or not (len(stack)==0)):
            
            while(curr != None):
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        
        return res