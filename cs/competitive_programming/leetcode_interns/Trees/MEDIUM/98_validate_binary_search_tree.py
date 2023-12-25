import math

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
TIME Complexity - O(N)
SPACE Complexity - O(1)
"""
    
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def valid(node, left, right):
            
            if node == None:
                return True
            
            if not(node.val > left and node.val < right):
                return False
        
            return (valid(node.left,left ,node.val) and valid(node.right, node.val, right))
                    
        
                
        return valid(root, float("-inf"), float("inf"))


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, l, r):
            if not node:
                return True
            if(not(node.val>l and node.val<r)):
                return False

            return (valid(node.left, l, node.val)) and (valid(node.right, node.val, r))


        return valid(root, -math.inf, math.inf)
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        res = []
        def helper(node):
            nonlocal res

            if not node:
                return
            
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        

        helper(root)
        l = len(res)

        for idx in range(len(res)-1):
            if(res[idx+1]-res[idx]>0):
                continue
            else:
                return False
        return True


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node, l, r):

            if not node:
                return True
            
            if not( (node.val>l) and (node.val<r) ):
                return False

            
            return ( (helper(node.left, l, node.val)) and helper(node.right, node.val, r) )


        return helper(root, -math.inf, math.inf)
