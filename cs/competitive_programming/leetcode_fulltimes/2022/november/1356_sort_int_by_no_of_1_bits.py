class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        store = {}
        
        for ele in arr:
            c = self.dec2bin( ele )
            if c not in store:
                store[c] = []
            store[c].append(ele)


        res = []

        for k in sorted(store.keys()):
            for v in sorted(store[k]):
                res.append(v)
    
        return res

    def dec2bin( self, num ):

        if num == 0:
            return 0
        
        ans = ""
        while( num>=1 ):
            ans += str(num&1)
            num = num >> 1
        
        return ans[::-1].count('1')
