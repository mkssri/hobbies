"""
Author: Murali Sriram
Date: 03/28/2023
Purpose: Murali wrote function to find intersection of 2 linked lists
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        pa, pb = headA, headB

        while(pa != pb):

            pa = headB if pa==None else pa.next
            pb = headA if pb==None else pb.next

        return pa
