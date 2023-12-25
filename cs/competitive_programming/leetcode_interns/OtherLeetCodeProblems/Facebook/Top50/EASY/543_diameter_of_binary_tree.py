from typing import Optional

# Definition for a binary tree node.

"""
Let N be the number of nodes in the tree.

Time complexity: O(N) This is because in our recursion function longestPath, we only enter and exit from each node once. 
We know this because each node is entered from its parent, and in a tree, nodes only have one parent.

Space complexity: O(N) The space complexity depends on the size of our implicit call stack during our DFS, which relates to the height of the tree. 
In the worst case, the tree is skewed so the height of the tree is O(N). If the tree is balanced, it'd be O(log N).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        diameter = 0
        
        def localPath(node):
            
            nonlocal diameter
            
            # Base Case
            if not node:
                return 0
            
            left_length = localPath(node.left)
            right_length = localPath(node.right)
            
            diameter = max(diameter, left_length+right_length)
            
            return max(left_length,right_length)+1
        
        localPath(root)
        return diameter
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def helper(node):
            nonlocal res

            if not node:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            res = max(res, l+r)

            return 1+max(l,r)
        
        helper(root)
        return res
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def helper(node):
            nonlocal res
            
            if not node:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            res = max(res, l+r)

            return 1+max(l,r)
        

        helper(root)
        return res
    
    
    
