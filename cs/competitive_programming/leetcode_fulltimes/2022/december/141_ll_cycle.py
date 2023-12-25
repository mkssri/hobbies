# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head==None:
            return False
        
        s_ptr, f_ptr = head, head.next

        while(s_ptr!=None and f_ptr!=None and f_ptr.next!=None):
            if s_ptr==f_ptr:
                return True
            s_ptr=s_ptr.next
            f_ptr=f_ptr.next.next
        
        return False