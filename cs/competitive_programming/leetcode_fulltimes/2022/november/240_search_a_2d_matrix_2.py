# Time Complexity: O(m*n)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for r in range(len( matrix )):
            for c in range(len( matrix[r] )):

                if matrix[r][c] == target:
                    return True

        return False

# Time Complexity: O(m+n)   
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r, c = len(matrix)-1, 0

        while( r>=0 and c<len(matrix[0]) ):
            
            ele = matrix[r][c]

            if( ele == target ):
                return True
            elif( ele < target ):
                c += 1
            else: # ele > target
                r -= 1

        return False