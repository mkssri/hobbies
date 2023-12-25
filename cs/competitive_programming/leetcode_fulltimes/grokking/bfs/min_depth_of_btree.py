from collections import deque

class TreeNode:
    
    def __init__( self, val ):
        self.val = val
        self.left = None
        self.right = None
        

def find_minimum_depth( root ):
    
    queue = deque()
    queue.append(root)
    
    min_depth = 0
    
    while( queue ):
        min_depth += 1
        level_nodes = len(queue)
        
        for _ in range(level_nodes):
            ele = queue.popleft()
            if not ele.left and not ele.right:
                return min_depth
            
            if ele.left:
                queue.append( ele.left )
            if ele.right:
                queue.append( ele.right )
            
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()