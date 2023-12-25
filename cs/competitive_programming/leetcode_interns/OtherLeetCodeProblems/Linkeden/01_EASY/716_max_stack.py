#!/usr/bin/python3
# Problem - https://leetcode.com/problems/max-stack/submissions/
# https://www.youtube.com/watch?v=WrIcFvGNnbM

import math 

class MaxStack:

    def __init__(self):
        self.stk = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        

    def pop(self) -> int:
        return self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]
    
    def retriveMaxAndIndex(self):
        
        len_of_stk = len(self.stk)
        x = -math.inf
        highValIndex = 0
        
        for i in range(0, len_of_stk):
            
            if self.stk[i] >= x:
                x, highValIndex = self.stk[i], i
                
                
        return x, highValIndex


    def peekMax(self) -> int:
        
        maxValue, highValIndex = self.retriveMaxAndIndex()
        return maxValue
        

    def popMax(self) -> int:
        maxValue, highValIndex = self.retriveMaxAndIndex()
        return self.stk.pop(highValIndex)        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()


### Optimized Solution

import math 

class MaxStack1:

    def __init__(self):
        self.stk = []
        

    def push(self, x: int) -> None:
        self.stk.append(x)
        

    def pop(self) -> int:
        return self.stk.pop()

    
    def top(self) -> int:
        return self.stk[-1]
    
    
    def peekMax(self) -> int:
        return max(self.stk)
        
        
    def popMax(self) -> int:

        val = self.peekMax()
        for x in range(-1, -len(self.stk)-1, -1):
            
            if self.stk[x] == val:
                del self.stk[x]
                break
                
        return val