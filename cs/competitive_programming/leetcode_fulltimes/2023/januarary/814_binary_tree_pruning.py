# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
      
        def nodeContainsOne(node)->bool:
          
          if not node:
            return False
          
          leftSubTreeContainsOne = nodeContainsOne(node.left)
          rightSubTreeContainsOne = nodeContainsOne(node.right)

          if not leftSubTreeContainsOne:
            node.left = None

          if not rightSubTreeContainsOne:
            node.right = None

          return node.val == 1 or leftSubTreeContainsOne or rightSubTreeContainsOne



        if nodeContainsOne(root):
          return root
        return None