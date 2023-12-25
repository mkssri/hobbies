from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val 
        self.left, self.right = None, None

def traverse( root ):
    
    if root is None:
        return None
    
    queue, res = deque(), deque()
    queue.append( root )
    
    while( queue ):
        curr_level = []
        num_of_items = len(queue)
        
        for _ in range( num_of_items ):
            ele = queue.popleft()
            curr_level.append( ele.val )
            
            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)
        res.appendleft(curr_level)
    
    return res
    

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: "+str(traverse(root)))

main()