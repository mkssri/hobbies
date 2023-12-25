#!/usr/bin/python3

# Link - https://leetcode.com/problems/min-stack/

class MinStack:
        
    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        
        If the stack is empty, then the min value
        must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
        
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
    
class MinStack1:
        
    def __init__(self):
        self.stk = []        

    def push(self, x: int) -> None:        
        
        # STACK EMPTY
        
        # First element is minimum elemet since no element is present 
        if len(self.stk) == 0:
            self.stk.append((x,x))
            return
        
        self.stk.append(( x, min(x, self.stk[-1][-1])))
        
        
    def pop(self) -> None:
        return self.stk.pop()[0]        

    def top(self) -> int:
        return self.stk[-1][0]        

    def getMin(self) -> int:
        return self.stk[-1][-1]
        
    