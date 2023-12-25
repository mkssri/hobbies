from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        out = []
        for i in range(1,n+1):
            out.append(self.checkForOutput(i))   
        
        
        return out
    
    def checkForOutput(self, i):
        
        if i%3 == 0 and i%5 == 0:
            return "FizzBuzz"
        elif i%3 == 0:
            return "Fizz"
        elif i%5 == 0:
            return "Buzz"
        else:
            return str(i)