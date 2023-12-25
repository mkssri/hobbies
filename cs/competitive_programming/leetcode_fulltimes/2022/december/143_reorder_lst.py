# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        #Find mid point
        s_ptr, f_ptr=head, head.next

        while(f_ptr and f_ptr.next):
            s_ptr=s_ptr.next
            f_ptr=f_ptr.next.next
        
        second=s_ptr.next
        prev=s_ptr.next=None
        curr=second
        while(curr):
            tmp=curr.next
            curr.next=prev
            prev=curr
            curr=tmp
        
        first,second=head,prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next=second
            second.next=tmp1
            first, second=tmp1, tmp2