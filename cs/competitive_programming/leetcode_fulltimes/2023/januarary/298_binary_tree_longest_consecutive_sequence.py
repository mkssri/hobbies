# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        

        res = 1

        def dfs(node, length):
            nonlocal res

            if not node:
                return

            if node.left and (node.left.val-node.val==1):
                dfs(node.left, length+1)
                res = max(res,length+1)
            else:
                dfs(node.left, 1)

            if node.right and (node.right.val-node.val==1):
                dfs(node.right, length+1)
                res = max(res,length+1)
            else:
                dfs(node.right, 1)


        dfs(root, 1)
        return res



class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        

        max_ = 0

        def dfs(node):

            nonlocal max_
            
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            if node.left and (node.left.val-node.val == 1):
                l += 1
            else:
                l = 1

            if node.right and (node.right.val-node.val == 1):
                r += 1
            else:
                r = 1

            max_ = max(l,r,max_)
            return max(l,r)


        dfs(root)
        return max_


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        res = 1

        def helper(node, l):
            nonlocal res

            if not node:
                return


            res = max(res, l)

            
            if(node.left and (node.left.val - node.val)==1):
                helper(node.left, l+1)
            else:
                helper(node.left, 1)

            if(node.right and (node.right.val-node.val)==1):
                helper(node.right, l+1)
            else:
                helper(node.right, 1)

        helper(root, 1)
        return res
