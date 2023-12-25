class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        sucessor = None

        while root:

            if p.val >= root.val:
                root = root.right
            else:
                sucessor = root
                root = root.left
        
        return sucessor