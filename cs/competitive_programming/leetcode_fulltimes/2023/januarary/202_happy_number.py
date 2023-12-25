class Solution:
    def isHappy(self, n: int) -> bool:

        def helper(n):
            tmp=0
            while(n>0):
                d=n%10
                tmp+=d*d
                n=n//10
            return tmp

        num_set=set()
        # num_set.add(n)
        while(n!=1):
            num_set.add(n)
            n=helper(n)
            if n==1:
                return True
            if n in num_set:
                return False
        return True