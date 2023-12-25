#!/usr/bin/python3


class Solution:

    def method1(self, s):
        res = []

        for x in range(0,len(s)):
            for y in range(x, len(s)):

                str1 = s[x:y+1]
                res.append(str1)

        return res


obj = Solution()

s = "abc"
res = obj.method1(s)
print(res)