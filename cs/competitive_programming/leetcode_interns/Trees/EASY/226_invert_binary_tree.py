#!/usr/bin/python3

# Link - https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
"""
Complexity Analysis

Since each node in the tree is visited only once, the time complexity is O(n)O, 
where n is the number of nodes in the tree. We cannot do better than that, since at the very least we have to 
visit each node to invert it.

Because of recursion, O(h) function calls will be placed on the stack in the worst case, 
where hh is the height of the tree. Because h\in O(n)h∈O(n), the space complexity is O(n).
"""       

# Approach 1 - RECURSIVE METHOD

class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root == None:
            return None
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        
        return root
    
"""
TIME COMPLEXITY - O(n)
Space Complexity - O(n)
"""    
# Approach 2 - ITERATIVE METHOD

class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root == None:
            return None
        
        queue = []
        queue.append(root)
        
        while( not(len(queue) == 0)):
            current = queue.pop(0)
            temp = current.left
            current.left = current.right
            current.right = temp
            
            if(current.left != None):
                queue.append(current.left)
            if(current.right != None):
                queue.append(current.right)
        
        return root