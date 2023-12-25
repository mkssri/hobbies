class TreeNode:
    
    def __init__( self, val, left=None, right=None ):
        self.val = val
        self.left = left
        self.right = right
        
def dfs( root, res, path ):
    
    if root is None:
        return
    
    path.append( str(root.val) )
    
    if root.left is None and root.right is None:
        res.append( list(path) )
        
    dfs( root.left, res, path )
    dfs( root.right, res, path )
    
    path.pop()
        
        
def sumOfPathNums( root ):
    
    res = [ ]
    dfs( root, res, [] )
    total = 0
    for ele in res:
        ele = int("".join(ele))
        total += ele
    return total
        

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(sumOfPathNums(root)))


main()
    