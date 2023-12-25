class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        flips, ones = 0, 0

        for c in s:
            if c=='0': 
                flips+=1
            else:
                ones+=1
            flips = min(flips, ones)
        return flips