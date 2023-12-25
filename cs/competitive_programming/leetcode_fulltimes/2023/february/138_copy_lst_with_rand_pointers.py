class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        #BASE CASE
        if not head:
            return None
        
        store = {}
        prev, curr = None, head

        while(curr):
            store[curr]=copy.copy(curr)

            if prev:
                store[prev].next = store[curr]

            prev, curr = curr, curr.next


        #Assigning Randomn pointers
        curr=head
        while(curr):
            if store[curr].random:
                store[curr].random = store[curr.random]
            curr = curr.next

        return store[head]

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head == None:
            return None

        prev, curr = None, head
        store= {}

        # Creating new Node
        # Using next pointer
        while(curr):
            store[curr] = Node(curr.val)
            if prev:
                store[prev].next = store[curr]
            prev=curr
            curr = curr.next

        curr = head
        while(curr):
            if curr.random != None:
                store[curr].random = store[curr.random]
            curr = curr.next
        
        return store[head]
