#!/usr/bin/python3

class Solution:
    def reverse(self, x: int) -> int:
        
        out_num = ""
        neg_num = False

        if x < 0:
            neg_num = True
        
        x = str(x)
        
        if neg_num:
            x = x[1:]

        print()
        
        for i in range(len(x)-1,-1,-1):
            
            out_num += str(x[i])

        out_num = int(out_num)
        
        if neg_num:
            out_num *= -1
        
        max_num = (2**31)-1
        min_num = -1*(2**31)
        
        # print("max_num - {} and min_num - {}".format(max_num, min_num))
        
        if out_num > max_num or out_num <= min_num:
            return 0
        else:
            return out_num
        