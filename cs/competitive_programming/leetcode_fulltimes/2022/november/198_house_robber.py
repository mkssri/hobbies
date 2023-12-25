class Solution:
    def rob(self, nums: List[int]) -> int:

        rob1, rob2 = 0, 0

        #[ rob1, rob2, n, n+1, n+2, n+3 ..... ]
        # At every level we have 2 options
        # option1: n+rob1
        # option2: rob2

        for n in nums:
            temp = max( n+rob1, rob2 )
            rob1 = rob2
            rob2 = temp
        
        return rob2

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        [ rob1, rob2, n, n+1, n+2, n+3 ]
        """
        rob1, rob2 = 0, 0

        for n in nums:
            # decision up to item having value: n
            tmp = max(rob1+n,rob2)
            rob1=rob2
            rob2=tmp
        return rob2
