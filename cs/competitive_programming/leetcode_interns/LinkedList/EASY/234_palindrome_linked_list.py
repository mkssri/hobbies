#!/usr/bin/python3

# Link - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
TIME Complexity - O(N)
SPACE Complexity - O(N)
"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        curr, fp,sp = head,head, head
        stk = []
        count = 0
        
    
        if fp.next == None or fp == None:
            return True
        
        while(curr != None):
            count += 1
            curr = curr.next
            
        print("count is {}".format(count))
        
        while(fp != None and fp.next != None):
            
            stk.append(sp.val)
            fp = fp.next.next
            sp = sp.next

        if count %2 != 0:
            sp = sp.next
            
            
        while(sp != None):
            
            if sp.val == stk.pop():
                sp = sp.next
            else:
                return False
        return True
    
    
    
