# Definition for singly-linked list.


"""
Time Complexity - O(N)
Space Complexity - O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode):
        
        
        if head == None:
            return None
        
        # Other cases
        
        prev = None
        
        while(head != None):
            
            current = head
            head = head.next
            current.next = prev
            prev = current
            
        
        return current
            
            
            