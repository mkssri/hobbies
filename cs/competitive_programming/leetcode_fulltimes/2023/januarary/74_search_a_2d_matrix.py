class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        data=[]
        R=len(matrix)
        C=len(matrix[R-1])

        for r in range(R):
            data+=matrix[r]

        l,r=0,len(data)-1

        while(l<=r):
            m=l+(r-l)//2
            ele=data[m]

            if ele==target:
                return True
            elif ele>target:
                r=m-1
            else:
                l=m+1
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        R=len(matrix)
        C=len(matrix[0])

        top,bot=0,R-1

        while(top<=bot):
            row=top+(bot-top)//2
            if target>matrix[row][-1]:
                top=row+1
            elif target<matrix[row][0]:
                bot=row-1
            else:
                break

        if not(top<=bot):
            return False

        row=top+(bot-top)//2

        s,e=0,C-1

        while(s<=e):
            m=s+(e-s)//2
            ele=matrix[row][m]
            if ele>target:
                e=m-1
            elif ele<target:
                s=m+1
            else:
                return True
        return False