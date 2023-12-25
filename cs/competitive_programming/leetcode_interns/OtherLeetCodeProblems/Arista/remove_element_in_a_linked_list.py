#!/usr/bin/python3

class Node():

    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Solution():

    def removeElements(self, head, ele):

        dummy_node = Node(0, head)
        prev_node = dummy_node
        current_node = head

        while current_node:

            nxt_node = current_node.next

            if current_node.value == ele:
                prev_node.next = nxt_node
            else:
                prev_node = current_node
            
            current_node = nxt_node
        
        return dummy_node.next



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

dummy = node1

while dummy:

    print(dummy.value)
    dummy = dummy.next

obj = Solution()

out = obj.removeElements(node1, 6)

print("########NEW##############")

dummy = out

while dummy:

    print(dummy.value)
    dummy = dummy.next




        