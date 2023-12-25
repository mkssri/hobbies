class Solution:
    def numberOfWays(self, s: str) -> int:
        
        """
        we need to search for following patterns:
        "101" or "010"
        """
        ones = zeros = 0
        before = []
        for c in s:
            if c == '1':
                before.append( zeros )
                ones += 1
            else:
                before.append( ones )
                zeros += 1

        after = []
        ones = zeros = 0
        for c in s[::-1]:
            if c == '1':
                after.append( zeros )
                ones += 1
            else:
                after.append( ones )
                zeros += 1

        ans = 0

        for i,j in zip(before, after[::-1]):
            ans += i*j

        return ans