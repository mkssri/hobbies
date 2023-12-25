#!/usr/bin/python3

#Link - https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
#MURALI Solution
# TIME COMPLEXITY - O(n)
# Space Complexity - O(1)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        
        
        prev = None
        
        while(head != None):
            
            current = head
            head = head.next
            
            current.next = prev
            prev = current
            
        return current

# LEETCODE Solution

# ITERATIVE SOLUTION
# TIME COMPLEXITY - O(N)
# SPACE COMPLEXITY - O(1)

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        current = head
        
        while(current != None):
            
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
            
        return prev

        



