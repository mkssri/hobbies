#!/usr/bin/python3

# Definition for a binary tree node.

from typing import Optional

# Recursive Approach

class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:

    def inOrderTraversal(self, root):
        res=[]
        
        def helper(node):
            nonlocal res
            
            if node:
                helper(node.right)
                res.append(node.val)
                helper(node.left)
        
        helper(root)
        return res
    
    
    def getMax(self, root):
        node = root
        while(node):
            cur_max = node
            node = node.right
        return cur_max if root.right else root  
    
    def getNextMax(self, node):
        next_max = None
        if node:
            if node.left != None:
                next_max = self.getMax(node.left)
            # search via parent
            else:
                par = node.parent
                while(par!=None and par.left==node):
                    node=par
                    par=par.parent
                next_max = par
        return next_max
    
    def printAllElementsDescendingOrder(self, root):
        node = self.getMax(root)
        res = []
        while(node):
            res.append(node.val)
            node=self.getNextMax(node)
        return res



"""
            2

    1                       4

                3                           5

            
        2.9                 3.1

    2.8     2.95         3.05      3.2
                                        
                                        3.3
"""

# Execution
        
#node initializations
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node3_1 = TreeNode(3.1)
node3_2 = TreeNode(3.2)
node3_3 = TreeNode(3.3)
node3_05 = TreeNode(3.05)
node2_9 = TreeNode(2.9)
node2_8 = TreeNode(2.8)
node2_95 = TreeNode(2.95)

#connections
node3_1.right = node3_2
node3_1.left = node3_05
node3_2.right = node3_3
node3_3.parent = node3_2
node3_2.parent = node3_1
node3_05.parent = node3_1
node3_1.parent = node3
node2.right = node4
node2.left = node1
node4.left = node3
node4.right = node5
node3.parent = node4
node3.right = node3_1
node3.left = node2_9
node2_9.left = node2_8
node2_9.right = node2_95
node2_8.parent = node2_9
node2_95.parent = node2_9
node2_9.parent = node3
node5.parent = node4
node4.parent = node2
node1.parent = node2


obj = Solution()
res = obj.inOrderTraversal(node2)
print("Inorder traversal output: {}".format(res))


res = obj.printAllElementsDescendingOrder(node2)
print("output: {}".format(res))