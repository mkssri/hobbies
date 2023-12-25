class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        def checkPrime(num):

            for i in range(2, int(math.sqrt(num))+1):
                if num%i == 0:
                    return False
            return True

        cnt = 0
        for i in range(2,n+1):
            if checkPrime(i):
                cnt += 1
        out = math.factorial(cnt)*math.factorial(n-cnt)
        out = out%(10**9 + 7)
        return out