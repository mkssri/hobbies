class Solution:
    def isValid(self, s: str) -> bool:

        store = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stk = []
        for idx in range( len(s) ):

            ele = s[idx]

            if ele in store:
                stk.append( ele )
            elif len(stk) != 0 and ele == store[ stk[-1] ]:
                stk.pop()
            else:
                return False

        return stk == []


class Solution:
    def isValid(self, s: str) -> bool:

        store = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stk = []

        for c in s:
            if c in store:
                stk.append(c)
            elif len(stk)!=0 and c==store[stk.pop()]:
                continue
            else:
                return False
                
        return len(stk)==0
