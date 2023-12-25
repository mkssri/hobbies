# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # First Element
        while head != None and head.val == val:
            head = head.next

        current = head

        # Later Elements
        while current != None:
            if current.next != None and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head