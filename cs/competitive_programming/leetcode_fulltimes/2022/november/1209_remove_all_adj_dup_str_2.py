class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # Stack, Each element is a 
        # list [ char, count ]
        stk = []

        for idx in range( len(s) ):

            if stk and stk[-1][0] == s[idx]:
                stk[-1][1] += 1
            else:
                stk.append( [ s[idx], 1 ] )


            if stk[-1][1] == k:
                stk.pop()
        

        res = ""

        for ele in stk:
            res += ele[0]*ele[1]
            
        return res