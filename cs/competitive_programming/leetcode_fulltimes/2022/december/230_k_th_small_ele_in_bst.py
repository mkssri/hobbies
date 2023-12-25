# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res=[]

        def inOrderTraverse(node):
            nonlocal res
            
            if node:
                inOrderTraverse(node.left)
                res.append(node.val)
                inOrderTraverse(node.right)
            

        inOrderTraverse(root)

        for i in range(len(res)):
            if i+1==k:
                return res[i]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n=0
        stk=[]
        curr=root

        while True:

            if curr:
                stk.append(curr)
                curr=curr.left
            elif(stk):
                curr=stk.pop()
                n+=1
                if n==k:
                    return curr.val
                curr=curr.right
            else:
                break
                
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        cnt=0
        res=""
        def in_order(node):
            nonlocal cnt, res
            if node:
                in_order(node.left)
                cnt+=1
                if cnt==k:
                    res=node.val
                    return
                in_order(node.right)


        in_order(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def helper(node):
            nonlocal res

            if not node:
                return

            helper(node.left)
            res.append(node.val)
            helper(node.right)
        
        helper(root)
        return res[k-1]
