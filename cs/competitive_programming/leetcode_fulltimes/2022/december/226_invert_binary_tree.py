# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        if root is None:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        tmp=root.left
        root.left=root.right
        root.right=tmp

        return root


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:



        def helper(node):

            if not node:
                return

            helper(node.left)
            helper(node.right)

            tmp = node.left
            node.left = node.right
            node.right = tmp


        helper(root)
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node):
            if not node:
                return

            helper(node.left)
            helper(node.right)

            tmp = node.left
            node.left = node.right
            node.right = tmp


            return node


        helper(root)
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node):

            if not node:
                return

            helper(node.left)
            helper(node.right)

            tmp = node.left
            node.left = node.right
            node.right = tmp

            return node

        return helper(root)
