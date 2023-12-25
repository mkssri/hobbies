# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inOrder(self, root, res):

        if root is None:
            return

        if root.left:
            res = self.inOrder( root.left, res )
        res.append( root.val )
        if root.right:
            res = self.inOrder( root.right, res )
        return res



    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        res = self.inOrder( root, res )
        
        prev = -math.inf

        print("res: {}".format(res))

        for idx in range( 0, len(res)-1 ):
            if res[idx+1] > res[idx]:
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

        def valid( node, left, right ):

            if node is None:
                return True

            if not(node.val < right and node.val> left):
                return False
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right )

    
        return valid(root, -math.inf, math.inf)
        



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

