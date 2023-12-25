# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        visited_nodes = set()
        tail = head

        while( tail ):

            ele = tail 

            if ele in visited_nodes:
                return True
            
            visited_nodes.add(ele)
            tail = tail.next

        return False
    
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None:
            return False

        slow_ptr, fast_ptr = head, head.next

        while( slow_ptr != fast_ptr ):

            if slow_ptr == None or fast_ptr == None or fast_ptr.next == None:
                return False

            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return True