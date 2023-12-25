#!/usr/bin/python3

# Link - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
HASH TABLE Approach
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(N)
"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        visited = set()
        
        node = head
        
        while node != None:
            
            if node in visited:
                return node
            
            else:
                visited.add(node)
                node = node.next
                
        return None
    
# Approach 2: Floyd's Tortoise and Hare
"""
TIME COMPLEXITY - O(N)
SPACE COMPLEXITY - O(1)
"""

class Solution1(object):
    
    def getIntersect(self, head):
        
        tortoise, hare = head, head
        
        # A fast pointer will either loop around a cycle and meet the slow pointer or reach the
        # the null at the end of a non-cyclic list
        
        while hare != None and hare.next != None:
            
            tortoise = tortoise.next
            hare = hare.next.next 
            
            if hare == tortoise:
                return tortoise
        
        return None
    
    
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some node. Otherwise, there is no cycle, so we cannot
        # find an entrace to a cycle
        
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrace to the cycle, we have two pointers traverse at the same speed -- one from the front of the
        # list,and other from the point of intersection
        
        ptr1 = head
        ptr2 = intersect
        
        while ptr1 != ptr2:
            
            ptr1 = ptr1.next 
            ptr2 = ptr2.next 
            
        return ptr1 
            
        