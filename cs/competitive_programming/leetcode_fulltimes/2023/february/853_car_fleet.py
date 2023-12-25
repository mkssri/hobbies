class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        lst = [ [p,s] for p,s in zip(position, speed) ]
        lst.sort(key=lambda x:x[0], reverse=True)

        stk = []
        for p,s in lst:
            time = (target-p)/s
            stk.append(time)

            if len(stk)>=2 and stk[-1]<=stk[-2]:
                stk.pop()
        
        return len(stk)