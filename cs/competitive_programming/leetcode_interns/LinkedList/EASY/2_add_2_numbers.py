#!/usr/bin/python3

# Link - https://leetcode.com/problems/add-two-numbers/


from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
"""
Time complexity : O(max(m, n)) Assume that mm and nn represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.
Space complexity : O(max(m,n)) The length of the new list is at most max(m,n)+1.
"""     
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummyHead = ListNode()
        p, q, curr = l1, l2, dummyHead
        carry = 0
        
        while(p != None or q != None):
            
            # TERNARY OPERATORS
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            
            sum = carry + x + y
            
            carry = sum//10
            curr.next = ListNode(sum%10)
            curr = curr.next
            
            if p != None:
                p = p.next
            if q != None:
                q = q.next
        
        if carry > 0:
            curr.next = ListNode(carry)
        
        return dummyHead.next
            
            
            


