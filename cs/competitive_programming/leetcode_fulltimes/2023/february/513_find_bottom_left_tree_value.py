# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        q = collections.deque([root])
        res = []

        while(q):
            tmp = []
            l = len(q)
            for _ in range(l):
                e = q.popleft()
                tmp.append(e.val)
                if e:
                    if e.left:
                        q.append(e.left)
                    if e.right:
                        q.append(e.right)
            res.append(tmp)
        
        return res[-1][0]