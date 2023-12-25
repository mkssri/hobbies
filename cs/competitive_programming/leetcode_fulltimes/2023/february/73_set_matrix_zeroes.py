class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        R = len(matrix)
        C = len(matrix[R-1])


        zero_lst = []
        for r in range(R):
            for c in range(C):
                if matrix[r][c]==0:
                    zero_lst.append((r,c))


        def helper(r,c):
            
            for c1 in range(C):
                matrix[r][c1]=0

            for r1 in range(R):
                matrix[r1][c]=0


        for r in range(R):
            for c in range(C):

                if (r,c) in zero_lst:
                    helper(r,c)