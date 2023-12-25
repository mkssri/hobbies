class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort( key=lambda x:x[0] )
        slots2.sort( key=lambda x:x[0] )

        i, j = 0, 0
        len_i, len_j = len(slots1), len(slots2)

        while( (i<len_i) and (j<len_j) ):

            s1, e1 = slots1[i]
            s2, e2 = slots2[j]

            if( (min(e1,e2)-max(s1,s2)) >= duration ):
                return [ max(s1,s2), max(s1,s2)+duration ]
            
            if e1>=e2:
                j+=1
            else:
                i+=1
        
        return []