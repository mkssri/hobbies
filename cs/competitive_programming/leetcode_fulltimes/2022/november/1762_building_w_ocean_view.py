class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        outDeque = collections.deque([])
        hMax = -1

        for i in range( len(heights)-1, -1, -1 ):

            ele = heights[i]

            if ele > hMax:
                outDeque.appendleft( i )
                hMax = ele
        
        return outDeque