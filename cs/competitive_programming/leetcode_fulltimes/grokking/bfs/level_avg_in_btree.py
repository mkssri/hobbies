from collections import deque


class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_level_averages( root ):
    
    queue = deque()
    queue.append( root )
    res = []
    
    while( queue ):
        
        level_nodes = len(queue)
        
        total = 0
        for _ in range( level_nodes ):
            ele = queue.popleft()
            total += ele.val
            
            if ele.left:
                queue.append( ele.left )
            if ele.right:
                queue.append( ele.right )
        res.append( total/level_nodes )
    
    return res

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()