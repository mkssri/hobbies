# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        x,y = head, head
        out,index = 0,0
        while x != None:            
            index += 1
            x = x.next

        index -= 1
        
        while y != None:            
            out += y.val*pow(2, index)
            index -= 1
            y = y.next
        print("Decimal value is {}".format(out))
        return out