"""
Read the Prefix expression in reverse order (from right to left)
If the symbol is an operand, then push it onto the Stack
If the symbol is an operator, then pop two operands from the Stack 
Create a string by concatenating the two operands and the operator after them. 
string = operand1 + operand2 + operator 
And push the resultant string back to Stack
Repeat the above steps until end of Prefix expression.
"""

s = "*-A/BC-/AKL"
stk = []
operators = set(['+','-','*','/','^'])
s = s[::-1]


for i in s:
    if i in operators:
        a = stk.pop()
        b = stk.pop()
        
        tmp = a+b+i
        stk.append(tmp)        
    else:
        stk.append(i)
        
# printing final output
# print(*stk)
print(stk[0])