#!/usr/bin/python3

# Link - https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        if head != None and head.next != None:
            sp,fp = head,head.next
        else:
            return False
        
        while(sp != None and sp.next != None and fp.next != None and fp.next.next != None):
            
            sp = sp.next
            fp = fp.next.next
            
            if sp == fp:
                return True
        return False

if __name__ == "__main__":
    
    obj = Solution()
    
    head = ListNode(3)
    head1 = ListNode(2)
    head2 = ListNode(0)
    head3 = ListNode(-4)
    
    head.next = head1
    head1.next = head2
    head2.next = head3
    # head3.next = head1

    # head = ListNode(1)
    # head1 = ListNode(2)
    # head.next = head1


    out = obj.hasCycle(head)
    print("out is {}".format(out))
        