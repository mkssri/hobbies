class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        n=""
        for x in digits:
            n+=str(x)
        n=int(n)
        n+=1
        n=str(n)
        return [ int(x) for x in n ]