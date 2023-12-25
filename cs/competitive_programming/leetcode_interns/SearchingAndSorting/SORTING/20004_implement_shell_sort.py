#!/usr/bin/python3



def shellSort(arr):
    
    sublistcount = len(arr)//2
    
    while sublistcount > 0:
        
        for start in range(sublistcount):
            
            gapInsertionSort(arr, start, sublistcount)
            
        sublistcount = sublistcount//2


def gapInsertionSort(arr, start, gap):
    
    for i in range(start+gap, len(arr), gap):
        
        currentvalue = arr[i]
        position = i
        
        while position >= gap and arr[position-gap] > currentvalue:
            
            arr[position] = arr[position-gap]
            position = position - gap
        
        arr[position] = currentvalue


def






if __name__ == "__main__":
    pass