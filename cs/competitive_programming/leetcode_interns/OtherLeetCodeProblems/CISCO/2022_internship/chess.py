#!/usr/bin/python3

class Solution:

    def func1(self, x):

        x = int(x)

        out1,out2,out = "","",""
        
        for i in range(0,x):

            if i % 2 == 0:
                out1 = out1 + "W"
                out2 = out2 + "B"
            else:
                out1 = out1 + "B"
                out2 = out2 + "W"

        
        for i in range(0,x):

            if i % 2 == 0 and i != x-1:
                out = out + out1 + "\n"
            elif i % 2 != 0 and i != x-1:
                out = out + out2 + "\n"
            elif i % 2 == 0 and i == x-1:
                out = out + out1
            elif i % 2 != 0 and i == x-1:
                out = out + out2


        print(out)



            

            




obj = Solution()
obj.func1(10)
