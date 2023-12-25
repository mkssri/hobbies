# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0

        def helper(node):
            nonlocal res # res scope is not limited to helper function(use as global)

            if node is None:return 0

            l_len=helper(node.left)
            r_len=helper(node.right)
            res=max(res, l_len+r_len)
            return max(l_len,r_len)+1
        
        helper(root)
        return res