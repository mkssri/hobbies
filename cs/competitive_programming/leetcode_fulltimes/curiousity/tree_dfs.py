class TreeNode:
    
    def __init__( self, val ):
        self.val = val
        self.left = None
        self.right = None
        
    
class Solution:
    
    def dfs( self, root, path, ans ):      
        
        if root is None:
            return
        
        path.append( root.val )
        
        if root.left == None and root.right == None:
            ans.append( list(path) )
            
        self.dfs( root.left, path, ans )
        self.dfs( root.right, path, ans )
        
        path.pop()
        

    
    def getDfs( self, root ):
        ans = []
        self.dfs( root, [], ans )
        return ans
    
    
class Iterative:
    
    def dfs(self, root):
        res=[]
        stk=[root]
        
        while stk:
            ele=stk.pop()
            res.append(ele.val)
            if ele.left:
                stk.append(ele.left)
            if ele.right:
                stk.append(ele.right)
        
        return res
        
        



node1 = TreeNode( 1 )
node2 = TreeNode( 2 )
node3 = TreeNode( 3 )
node4 = TreeNode( 4 )
node5 = TreeNode( 5 )
node6 = TreeNode( 6 )
node7 = TreeNode( 7 )

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node4.left, node4.right = None, None
node5.left, node5.right = None, None
node6.left, node6.right = None, None
node7.left, node7.right = None, None

# obj = Solution()
# res = obj.getDfs( node1 )
# print("res: {}".format(res))

"""

        1
      =   = 
    2       3
    =       =    
  4   5   6    7

"""

obj = Iterative()
res = obj.dfs( node1 )
print("res: {}".format(res))