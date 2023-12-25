from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None
    
def traverse( root ):
    
    res = []
    queue = deque()
    queue.append( root )
    left_to_right = True
    
    while( queue ):
        
        curr_level = deque()
        traverse_len = len(queue)
        
        for _ in range( traverse_len ):
            
            ele = queue.popleft()
            
            if left_to_right:
                curr_level.append(ele.val)    
            else:
                curr_level.appendleft(ele.val)
            

            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)
        
        res.append( curr_level )
        left_to_right = not left_to_right

    
    return res

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()