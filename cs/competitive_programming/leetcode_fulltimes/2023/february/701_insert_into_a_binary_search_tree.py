# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root: return TreeNode(val)

        def helper(node, val):
            
            if node.val < val:

                if not node.right:
                    node.right = TreeNode(val)
                else:
                    helper(node.right, val)

            else:

                if not node.left:
                    node.left = TreeNode(val)
                else:
                    helper(node.left, val)

        helper(root, val)
        return root