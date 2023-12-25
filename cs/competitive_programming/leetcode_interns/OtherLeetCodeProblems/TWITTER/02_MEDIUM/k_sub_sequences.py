#!/usr/bin/python3

# Simple Idea - for every element check if "number of sublists" <  count of every element in a array

from collections import Counter

class Solution:

    def solve(self, k, nums):
        if k == 0 or len(nums) == 0:
            return True
        if len(nums)%k != 0:
            return False
        counter = Counter(nums)
        print("counter - {}".format(counter))

        for entry in counter:
            # print("entry is {}".format(entry))

            if counter[entry] > len(nums)/k:
                return False
        return True





if __name__ == '__main__':
    obj = Solution()
    print(obj.solve(2,[1,2,3,4])) #yes
    # print(obj.solve(2,[1,2,3,3])) #yes
    # print(obj.solve(3,[1,2,3,4])) #no
    # print(obj.solve(3,[3,3,3,6,6,6,9,9,9]))#yes
    # print(obj.solve(1,[]))#yes
    # print(obj.solve(1,[1]))#yes
    # print(obj.solve(2,[1,2]))#yes