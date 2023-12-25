#!/usr/bin/python3

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time complexity - O(n^2)

class Solution:
    
    def inOrder(self, root, lst):

        if root is None:
            return
        
        self.inOrder(root.left, lst)
        lst.append(root.val)
        self.inOrder(root.right, lst)
        
        return lst
        
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        lst = self.inOrder(root, [])
        
        if len(lst) <= 1:
            return False

        x = 0
        y = len(lst)-1
        
        while x < y:
            
            if lst[x] + lst[y] < k:
                x += 1
            elif lst[x] + lst[y] > k:
                y -= 1
            else:
                print("x and y - ({},{})".format(x,y))
                return True
        
        return False
                
                

    

# Time complexity - O(n^2)

# Working Solution...    
    
#         for p in range(0, len(lst)):
#             for q in range(p+1, len(lst)):
                
#                 if lst[p] + lst[q] == k:
#                     print("p and q are - ({},{})".format(p,q))
#                     return True
#                 else:
#                     continue
#         return False
                

        
class Solution2:
        
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        
        set1 = set()
        
        return self.find(root, k, set1)
    
    def find(self, root, k, set1):
        
        if root == None:
            return False
        
        if (k - root.val) in set1:
            return True
        
        set1.add(root.val)
        
        return self.find(root.left, k, set1) or self.find(root.right, k, set1)
        
        
