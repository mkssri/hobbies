class llNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
        
node1 = llNode(1)
node2 = llNode(2)

node3 = llNode(3)
node4 = llNode(4)

node5 = llNode(5)
node6 = llNode(6)

node7 = llNode(7)
node8 = llNode(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node4


class Solution:
    
    def detectCycle( self, head ):
        
        slow = head
        fast = head
        
        while( fast != None and fast.next != None ):
            
            slow = slow.next
            fast = fast.next.next
            
            if( slow == fast ):
                print("Cycle detected!")
                return slow
            
        print("No cycle detected!")
        return None
    
    def detectCycleNode( self, head, match_node ):
        
        # match_node = self.detectCycle( head )
        start_node = head
        
        prev_node = None
        while( match_node != start_node ):
            
            prev_node = match_node
            match_node = match_node.next
            start_node = start_node.next
        
        return ( prev_node, match_node )
    
    def removeCycle( self, head, match_node ):
        
        ( prev_node, match_node ) = self.detectCycleNode( head, match_node )
        prev_node.next = None
        
        self.detectCycle( head )
        

obj = Solution()
head = node1
res = obj.detectCycle( head )
if res is None:
    print("res: {}".format(res) )
else:
    print( "res.val: {} and next.val: {}".format(res.val, res.next.val) )


# ( prev_node, match_node ) = obj.detectCycleNode( head )
obj.removeCycle( head, res )
# print("match_node:- {}".format(match_node.val))        
# print("prev_node:- {}".format(prev_node.val))        
            
    
    
    
    






        