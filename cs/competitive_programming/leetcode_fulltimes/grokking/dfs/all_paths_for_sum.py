class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    
def dfs( root, path, ans, targetSum ):

    if root is None:
        return
    
    path.append( root.val )

    if ((root.left == None) and (root.right == None) and (targetSum == root.val)):
        ans.append(list(path))
    
    dfs( root.left, path, ans, targetSum-root.val)
    dfs( root.right, path, ans, targetSum-root.val)

    path.pop()



def pathSum( root, targetSum ):
    ans = []
    dfs( root, [], ans, targetSum )
    return ans
    
def main():
    
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(pathSum(root, required_sum)))


main()