class Solution:
    
    def dfs( self, root, path, ans, targetSum ):

        if root is None:
            return
        
        path.append( root.val )

        if ((root.left == None) and (root.right == None) and (targetSum == root.val)):
            ans.append(list(path))
        
        self.dfs( root.left, path, ans, targetSum-root.val)
        self.dfs( root.right, path, ans, targetSum-root.val)

        path.pop()



    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        self.dfs( root, [], ans, targetSum )
        return ans