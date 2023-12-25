class MinStack:
    
    def __init__(self):
        self.stk, self.min_stk = [], []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.min_stk)!=0:
            self.min_stk.append(min(val,self.min_stk[-1])) 
        else:
            self.min_stk.append(val)

    def pop(self) -> None:
        if len(self.stk)!=0 and len(self.min_stk)!=0:
            self.stk.pop()
            self.min_stk.pop()

    def top(self) -> int:
        if len(self.stk)!=0:
            return self.stk[-1]

    def getMin(self) -> int:
        if len(self.min_stk)!=0:
            return self.min_stk[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()