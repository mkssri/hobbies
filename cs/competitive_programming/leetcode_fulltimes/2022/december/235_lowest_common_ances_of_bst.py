# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        curr_node = root

        while(curr_node):
            if(curr_node.val>p.val and curr_node.val>q.val):
                curr_node=curr_node.left
            elif(curr_node.val<p.val and curr_node.val<q.val):
                curr_node=curr_node.right
            else:
                return curr_node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while(curr!=None):

            if((curr.val>p.val) and (curr.val>q.val)):
                curr = curr.left
            elif((curr.val<p.val) and (curr.val<q.val)):
                curr = curr.right
            else:
                """
                 if((curr.val==p.val) or if(curr.val==q.val))
                 or  if( (curr.val>p.val) and (curr.val<q.val))
                 or  if( (curr.val<p.val) and (curr.val>q.val))
                """
                return curr
