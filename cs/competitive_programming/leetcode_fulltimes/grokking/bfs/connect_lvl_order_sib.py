from __future__ import print_function
from collections import deque

class TreeNode:
    
    def __init__( self, val ):
        self.val = val
        self.left, self.right, self.next = None, None, None
    
    #TODO
    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()
        
        
def connect_level_order_siblings(root):
    if root is None:
        return
    
    queue = deque()
    queue.append( root )
    
    while( queue ):
        prev_node = None
        level_size = len(queue)
        
        for _ in range(level_size):
            curr_node = queue.popleft()
            
            if prev_node:
                prev_node.next = curr_node
            prev_node = curr_node
            
            if curr_node.left:
                queue.append( curr_node.left )
            if curr_node.right:
                queue.append( curr_node.right )