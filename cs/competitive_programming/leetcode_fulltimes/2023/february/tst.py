
def superStack(operations):
    
    n = len(operations)
    stk = 0
    
    
    for i in range(1,n+1):
        
        oper = operations[i]
        
        if oper.startswith("push"):
            val = oper.split(' ')[1]
            stk.append(int(val))
        elif oper.startswith("pop"):
            if(len(stk)!=0):
                stk.pop()
        elif oper.startswith("inc"):
            tmp = oper.split(' ')
            
            idx = tmp[1]
            val = tmp[2]
            
            modify_len = min(len(stk)-1, idx)
            
            for n_i in range(modify_len+1):
                stk[n_i] += 1

        
        if(len(stk)==0):
            print("EMPTY")
        else:
            print(stk[-1])