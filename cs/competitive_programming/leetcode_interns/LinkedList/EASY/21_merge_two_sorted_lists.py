#!/usr/bin/python3

# Link - https://leetcode.com/problems/merge-two-sorted-lists/

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ITERATIVE Solution
# Time complexity : O(n + m)
# Space complexity : O(1)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        prevHead = ListNode(-1)
        
        prev = prevHead
        
        while(l1 and l2):
            
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            
            prev = prev.next
            
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        
        prev.next = l1 if l1 != None else l2
        
        return prevHead.next

# RECURSIVE Solution
# Time Complexity - O(n+m)
# Space Complexity - O(n+m)

class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
        
        
    