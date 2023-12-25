# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node, curr_sum):
            
            if not node:
                return False
            
            curr_sum += node.val

            if not node.left and not node.right:
                return curr_sum == targetSum

            return helper(node.left, curr_sum) or helper(node.right, curr_sum) 
        

        return helper(root,0)