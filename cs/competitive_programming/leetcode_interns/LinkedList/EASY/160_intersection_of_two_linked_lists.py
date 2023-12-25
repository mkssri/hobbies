#!/usr/bin/python3

# Link - https://leetcode.com/problems/intersection-of-two-linked-lists/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
TIME COMPLEXITY - O(N*M)
SPACE COMPLEXITY - O(1)
"""

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        curr_b = headB
        curr_a = headA
        
        while(curr_a != None):
            
            curr_b = headB
        
            while(curr_b != None):
                
                if curr_a == curr_b:
                    return curr_a
                
                curr_b = curr_b.next
            
            curr_a = curr_a.next
            
        
        return None

# USING HASH TABLE
"""
TIME COMPLEXITY - O(N+M)
SPACE COMPLEXITY - O(N) or O(M)
"""

class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        set_b = set()
        
        curr_b = headB
        
        while(curr_b != None):
            set_b.add(curr_b)
            curr_b = curr_b.next
            
        curr_a = headA
        
        while(curr_a != None):
            
            if curr_a in set_b:
                return curr_a
            curr_a = curr_a.next
            
        return None

# Approach 3: Two Pointers (BEST APPROACH) 

"""
once pointer becomes none start it from other Linked List..so by 2nd iteration..everything will be sorted

TIME COMPLEXITY - O(N+M)
SPACE COMPLEXITY - O(1)
"""

class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        p_a, p_b = headA, headB
        
        while(p_a != p_b):
            
            p_a = headB if p_a == None else p_a.next
            p_b = headA if p_b == None else p_b.next
        
        return p_a

    


if __name__ == "__main__":
    
    # [4,1,8,4,5]
    # [5,6,1,8,4,5]
    
    obj = Solution()
    obj1 = Solution1()
    obj2 = Solution2()
    
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    
    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = ListNode(8)
    headB.next.next.next.next = ListNode(4)
    headB.next.next.next.next.next = ListNode(5)

    
    
    out = obj.getIntersectionNode(headA, headB)
    
    out1 = obj1.getIntersectionNode(headA, headB)

    out2 = obj2.getIntersectionNode(headA, headB)

    
    
    print(out)
    print(out1)
    print(out2)