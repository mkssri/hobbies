class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        store = collections.defaultdict(int)
        for row, val in reservedSeats:

            store[row] = store[row] | 1<<(val-1)

        res = 2*n

        """
        # Possibilities
        1000000001 = 513 -> 2 values
        1000011111 = 16+8+4+2+1 =  543 -> 1 value
        1111100001 = 1+32+64+128+256+512 = 993 -> 1 value
        1110000111 = 512+256+128+4+2+1 =  903 -> 1 value
        """

        for row, val in store.items():

            if (val | 513) == 513:
                continue
            elif (val | 543) == 543 or (val | 993) == 993 or (val|903)==903:
                res -= 1
            else:
                res -= 2
        
        return res