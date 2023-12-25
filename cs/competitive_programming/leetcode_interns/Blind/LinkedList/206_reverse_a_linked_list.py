#!/usr/bin/python3

class LinkedList():

    def __init__(self, val):

        self.val = val
        self.next = None


class Solution():

    def reverseLinkedList(self, head):

        prev_node = None

        while head:

            temp_node = head
            head = head.next
            temp_node.next = prev_node
            prev_node = temp_node
        
        return prev_node

node1 = LinkedList(1)
node2 = LinkedList(2)
node3 = LinkedList(3)


node1.next = node2
node2.next = node3

obj1 = Solution()
head_out = obj1.reverseLinkedList(node1)

while head_out:

    print(head_out.val)
    head_out = head_out.next





        