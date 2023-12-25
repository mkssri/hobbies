import collections

class TreeNode:
    
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Sol:
    
    def helper(self,node, lst):
        
        if len(lst)==0:
            return None
        
        n=len(lst)-1
        m = n//2
        
        left_child_idx = (m-1)//2
        right_child_idx = m+(n-m-1)//2
        
        node.left = TreeNode(lst[left_child_idx])
        node.right = TreeNode(lst[right_child_idx])
        
        self.helper(node.left, lst[0:m-1])
        self.helper(node.right, lst[m+1:])

        
    def main(self, lst):
        
        n = len(lst)
        m = (n-1)//2
        root = TreeNode(lst[m])
        node = root
        self.helper(node, lst)
        return root
    

    def bfs(self,root):
        
        q = collections.deque([root])
        res=[]
        while(q):
            l = len(q)
            lst=[]
            for _ in range(l):
                ele = q.popleft()
                if ele:
                    lst.append(ele.val)
                    if ele.left:
                        q.append(ele.left)
                    if ele.right:
                        q.append(ele.right)

            res.append(lst)
        return res
        
        
        
        
obj = Sol()
lst = [1,2,3,4,5,6,7,8,9]
root = obj.main(lst)
print("--")
print(root.val)
print(root.left.val)
print(root.right.val)
print("--")

"""
[1,2,3,4,5,6,7,8,9]


                           5
                 2                   7
            1        3            6      8
                        4                   9



"""



res = obj.bfs(root)

print("res: {}".format(res))

"""
        1
    2       3
4       5  6  7
"""
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

print("----")
print("----")


res = obj.bfs(node1)

print("res: {}".format(res))







        
        
"""

          5
    3            7
1       3      7   9


"""
        
        
        
        
        