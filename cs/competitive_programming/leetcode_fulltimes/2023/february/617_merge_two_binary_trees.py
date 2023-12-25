# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:


        def helper(n1, n2):

            if((not n1) and (not n2)):
                return

            if(not n1 and n2):
                root = TreeNode(n2.val)

            if(not n2 and n1):
                root = TreeNode(n1.val)

            if(n1 and n2):
                root = TreeNode(n1.val+n2.val)
            
            if(n1 and n2):
                root.left = helper(n1.left, n2.left)
                root.right = helper(n1.right, n2.right)
            elif(not n2):
                root.left = helper(n1.left, None)
                root.right = helper(n1.right, None)
            elif(not n1):
                root.left = helper(None, n2.left)
                root.right = helper(None, n2.right)


            return root

        
        return helper(root1, root2)