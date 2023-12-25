#/usr/bin/python3


class Solution:
    def hammingWeight(self, n: int) -> int:


        bits = 0
        mask = 1
        
        for x in range(0,32):
            
            if (n & mask) != 0:
                bits += 1
            
            mask = mask << 1
                
        return bits

class Solution1:
    def hammingWeight(self, n: int) -> int:
        
        bits = 0
        
        mask = 1
        
        for x in range(32):
            
            if (n & mask) == mask:
                bits += 1
                print(bits)
            
            mask = mask << 1
        
        return bits
        


class Solution2:
    def hammingWeight(self, n: int) -> int:

        """
        numbers seperated by 1 are different by 1 bit
        """

        res = 0
        
        
        while n != 0:
            
            res += 1
            
            n = n & (n-1)
            
        return res
        
class Solution:
    def hammingWeight(self, n: int) -> int:

        res = 0
        while(n>0):
            if(n%2==1):
                res +=1
            n = n>>1
        return res
