def main():
    
    lst = [(5,4),(4,3),(3,2),(2,1)]
    
    n = len(lst)
    
    print("Before lst: {}".format(lst))
    
    for i in range(0, n):
        for j in range(0, n-i-1):
            if(lst[j][1]>lst[j+1][1]):
                tmp = lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=tmp
    
                
    print("After lst: {}".format(lst))



if __name__ == "__main__":
    main()