class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res=[0]

        for i in range(1,n+1):
            res.append(res[i//2]+i%2)
        return res
    
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res=[0]*(n+1)

        for i in range(1,n+1):
            res[i]= res[i//2]+i%2
        return res
    
class Solution:
    def countBits(self, n: int) -> List[int]:

        res=[]
        def helper(n):
            cnt=0
            while(n>0):
                if(n&1)==1:
                    cnt+=1
                n=n>>1
            return cnt
        
        for i in range(n+1):
            res.append(helper(i))
        
        return res