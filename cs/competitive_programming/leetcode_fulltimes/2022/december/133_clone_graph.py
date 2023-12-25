"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        store={}
        def dfs(node):
            if node in store:
                return store[node]
            
            store[node] = Node(node.val)
            for nei in node.neighbors:
                store[node].neighbors.append(dfs(nei))
            return store[node]
            

        
        return dfs(node) if node else None