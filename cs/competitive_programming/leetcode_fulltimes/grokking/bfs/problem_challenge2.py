from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def tree_right_view( root ):
    
    if root == None:
        return
    
    queue = deque()
    queue.append( root )
    res = []
    
    
    while( queue ):
        level_size = len(queue)
        
        for i in range( level_size ):
            curr_node = queue.popleft()
            
            if i == level_size-1:
                res.append( curr_node )
            
            if curr_node.left:
                queue.append(curr_node.left)
            
            if curr_node.right:
                queue.append(curr_node.right)
    return res

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
   print(str(node.val))


main()

            
            
