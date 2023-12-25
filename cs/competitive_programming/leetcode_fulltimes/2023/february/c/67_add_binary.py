class Solution:
    def addBinary(self, a: str, b: str) -> str:

        a = int(a,2)
        b = int(b,2)

        c = 0

        while(b>0):
            c = (a&b)<<1
            a = a^b
            b = c
        
        return bin(a)[2:]