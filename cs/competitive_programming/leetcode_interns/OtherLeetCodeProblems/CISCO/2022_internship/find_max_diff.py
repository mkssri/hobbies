#!/usr/bin/python3
import math


class Solution:
    def findMax(self, lst):

        min_ele = math.inf
        max_diff = -math.inf

        no_of_elements = len(lst)

        for i in range(0, no_of_elements):
            for j in range(0,no_of_elements):

                diff = lst[j] - lst[i]

                max_diff = max(max_diff, diff)
        
        return max_diff


class Solution1:
    def findMax(self, lst):

        min_ele = lst[0]
        max_diff = lst[1] - lst[0]

        for x in range(1,len(lst)):

            if max_diff < (lst[x] - min_ele):
                max_diff = lst[x] - min_ele

            if min_ele > lst[x]:
                min_ele = lst[x]

        return max_diff


if __name__ == "__main__":

    # obj1 = Solution()

    # lst = [1,2,3,6,5,0]
    # out = obj1.findMax(lst)

    # print(out)


    obj1 = Solution1()

    lst = [1,2,3,6,5,0]
    out = obj1.findMax(lst)

    print(out)


    obj = Solution()

    lst = [1,2,3,6,5,0]
    out = obj.findMax(lst)

    print(out)





        
