# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def helper(node):

            if not node: return [True, 0]
            
            left = helper(node.left)
            right = helper(node.right)
            balanced = (left[0] and right[0] and abs(left[1]-right[1])<=1)
            h = 1+max(left[1],right[1])
            
            return [ balanced, h ]

        return helper(root)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):

            if not node:
                return [True,0]
            
            l = helper(node.left)
            r = helper(node.right)

            balanced = (l[0] and r[0] and (abs(l[1]-r[1])<=1))
            h = 1+max(l[1],r[1])

            return [balanced, h]
        
        return helper(root)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        res = True

        def helper(node):
            nonlocal res

            if not node:
                return 0
            
            l = helper(node.left)
            r = helper(node.right)

            res = (res and abs(l-r)<=1)
            return 1+max(l,r)
        
        helper(root)
        return res
