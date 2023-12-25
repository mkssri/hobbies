#!/usr/bin/python3

# Link - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length, count = 0, 0
        current1 = head
        current2 = head

        
        while current1 != None:
        
            length += 1
            current1 = current1.next
            
        
        node_level_to_delete = length - n 
        print("node_level_to_delete - {}".format(node_level_to_delete))
        
        if node_level_to_delete == 0:
            return head.next
        
        prev = None
        while current2 != None:
            prev = current2
            count += 1
            current2 = current2.next
            
            if count == node_level_to_delete:
                print("prev.val - {}".format(prev.val))
                prev.next = current2.next
                return head
            
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""         
class SolutionV1(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = ListNode()
        dummy.next = head
        
        length = 0
        
        first = head
        
        while first != None:
            length += 1
            first = first.next
            
        
        length -= n
        
        first = dummy
        
        while(length > 0):
            length -= 1
            first = first.next
        
        first.next = first.next.next
        
        return dummy.next
    
    
# Approach 2: One pass algorithm
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
""" 
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy
        
        # Advances first pointer so that the gap between first and second is n nodes apart

        for i in range(1,n+2):
            first = first.next

        # Move first to the end, maintaining the gap
        # while loop will stop when first pointer reaches None
        while(first != None):
            first = first.next
            second = second.next
        
        # After above while loop second pointer will be on just previous element of "element we want to remove"
        # Below statement helps to remove linking, delete the element we wanted to remove
        second.next = second.next.next
        
        return dummy.next
