from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res=[]
        l = len(digits)

        store={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"],
        }



        def helper(i, cur):

            if len(cur)==l:
                res.append(cur)
                return

            
            for c in store[digits[i]]:
                helper(i+1, cur+c)



        if digits:
            helper(0, "")
        
        return res