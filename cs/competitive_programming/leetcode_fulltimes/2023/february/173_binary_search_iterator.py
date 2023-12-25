# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def helper(self,node):
        while node:
            self.stk.append(node)
            node=node.left

    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        if root:
            self.helper(root)

    def next(self) -> int:
        res = self.stk.pop()
        node = res.right
        if node:
            self.helper(node)
        return res.val

    def hasNext(self) -> bool:
        return self.stk != []
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
