class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst = []
        end = n//2
        if n%2 == 0:
            for i in range(1,end+1):
                lst.append(i)
                lst.append(-i)
        else:
            if n==1:
                lst.append(0)
            else:
                s=0
                for i in range(1, n-1 ):
                    s += i
                    lst.append(i)
                lst.append(-1)
                lst.append(1-s)
        
        return lst