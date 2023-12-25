class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def helper(ele1,ele2,op):

            if op=='+':
                return ele1+ele2
            elif op=='-':
                return ele1-ele2
            elif op=='*':
                return ele1*ele2
            else: # division(/)
                return int((ele1/ele2))

        n = len(tokens)

        if(n>1):

            stk = []
            operators = set()
            operators.add('+')
            operators.add('-')
            operators.add('*')
            operators.add('/')


            for i in range(n):

                if tokens[i] not in operators:
                    stk.append(tokens[i])
                else:
                    ele2=int(stk.pop())
                    ele1=int(stk.pop())
                    stk.append(helper(ele1,ele2,tokens[i]))
            
            return stk[-1]
        else:
            return int(tokens[-1])