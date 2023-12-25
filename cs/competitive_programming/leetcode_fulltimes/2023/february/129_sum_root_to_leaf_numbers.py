# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        tmp = ""
        c = 0

        def helper(node, tmp):
            nonlocal c

            if(not node):
                return
            
            tmp += str(node.val)
            
            if node.left:
                helper(node.left, tmp)
            if node.right:
                helper(node.right, tmp)
            if((not node.left) and (not node.right)):
                c = c + int(tmp)

        helper(root, "")
        
        return c


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        res = []
        tmp = ""

        def helper(node, tmp):


            if((not node.left) and (not node.right)):
                tmp += str(node.val)
                res.append(tmp)
                return
            
            tmp += str(node.val)
            if node.left:
                helper(node.left, tmp)
            if node.right:
                helper(node.right, tmp)

        helper(root, "")

        print("res: {}".format(res))

        c = 0

        for n in res:
            c += int(n)
        
        return c