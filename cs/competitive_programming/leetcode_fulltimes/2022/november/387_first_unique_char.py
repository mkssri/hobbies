class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        idx = -1
        visited_set = set()

        for i in range( len(s) ):
            ele = s[i]

            if( ele not in visited_set and ele not in s[i+1:] ):
                idx = i
                break
            visited_set.add( ele )

        return idx 