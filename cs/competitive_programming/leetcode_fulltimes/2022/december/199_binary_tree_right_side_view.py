# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        q=deque()
        q.append(root)

        while(q):
            total_ele=len(q)
            tmp=[]
            for i in range(total_ele):
                ele=q.popleft()
                if ele:
                    tmp.append(ele.val)
                    if ele.left:
                        q.append(ele.left)
                    if ele.right:
                        q.append(ele.right)
            if tmp!=[]:
                res.append(tmp[-1])
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        q = collections.deque([root])

        while(q):
            tmp = []
            l = len(q)
            for _ in range(l):
                ele = q.popleft()
                if ele:
                    tmp.append(ele.val)
                    if ele.left:
                        q.append(ele.left)
                    if ele.right:
                        q.append(ele.right)

            if(len(tmp)!=0):
                res.append(tmp[-1])
        
        return res
