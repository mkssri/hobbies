# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(p,q):

            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        q = collections.deque([root])

        while q:

            l = len(q)

            for _ in range(l):
                node = q.popleft()
                if node.val == subRoot.val and isSameTree(node, subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, p,q):

        if not p and not q:
            return True
        
        if (p and q and p.val==q.val):
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        if not subRoot:
            return True
        
        if not root:
            return False

        if self.isSameTree(root,subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(n1, n2):

            if not n1 and not n2:
                return True
            
            if not n1 or not n2 or n1.val != n2.val:
                return False
            
            return (helper(n1.left, n2.left) and helper(n1.right, n2.right))


        q = collections.deque([root])
        nroot = subRoot

        while(q):

            l = len(q)

            for _ in range(l):
                
                ele = q.popleft()

                if ele.val == nroot.val:
                    if(helper(ele, nroot)):
                        return True

                if ele:
                    if ele.left:
                        q.append(ele.left)
                    if ele.right:
                        q.append(ele.right)

        return False
