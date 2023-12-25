class Solution:
    def numSteps(self, s: str) -> int:

        def binToNum():
            n_len = len(s)
            total = 0

            for i,val in enumerate(s):

                idx = n_len-(i+1)
                total += int(val)*(2**idx)
            
            return total
        
        def solve(total):

            cnt = 0
            while(total != 1):
                cnt += 1
                if total%2 == 0:
                    total = total//2
                else:
                    total = total+1
            
            return cnt
        
        total = binToNum()

        return solve(total)