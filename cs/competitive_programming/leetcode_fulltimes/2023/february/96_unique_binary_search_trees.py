class Solution:
    def numTrees(self, n: int) -> int:

        num_trees = [1]*(n+1)
        
        """
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        """

        """
        To compute for nodes=4
        
        left[0]*right[3] + left[1]*right[2] + left[2]*right[1] + left[3]*right[0]
        """

        for nodes in range(2, n+1):
            total = 0
            for root in range(1, nodes+1):
                left = root-1
                right = nodes-root
                total += (num_trees[left]*num_trees[right])
            num_trees[nodes]=total

        return num_trees[n]