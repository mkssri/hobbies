# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        
        def helper(node):    
            
            nonlocal res

            if not node:
                return
            
            helper(node.left)
            res.append(node.val)
            helper(node.right)

        helper(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Inorder:
left, root, right
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def helper(node):
            if not node:
                return

            if node.left:
                helper(node.left)
            res.append(node.val)
            if node.right:
                helper(node.right)
        
        helper(root)
        return res
