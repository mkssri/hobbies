#!/usr/bin/python3

# Solution - https://www.youtube.com/watch?v=KkEDJ5EwODo

from typing import List


    
class Solution:

    """
    Time Complexity - O(N^2)
    Space Complexity - O(1)
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        
        count = 0
        for i in range(0,len(flowerbed)):
            if flowerbed[i] == 0:
                prev = 0 if (i == 0 or flowerbed[i-1] == 0) else 1
                next = 0 if (i == len(flowerbed)-1 or flowerbed[i+1] == 0) else 1

                if prev == 0 and next == 0:
                    # print("i is {}".format(i))
                    flowerbed[i] = 1
                    count += 1

        # print("count is {}".format(count))
        return count >= n



obj = Solution()
flowerbed, n = [0,0,0],3
out = obj.canPlaceFlowers(flowerbed, n)
print(out)
                



        