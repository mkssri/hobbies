#!/usr/bin/python3
"""
Insertion sort builds the final sorted array (or list) one item at a time. It is much less efficient on large Lists than more advanced
algorithsm such as quick sort, heap sort or merge sort
"""


def insertionSort(arr):
    
    for i in range(1, len(arr)):
        
        current_value = arr[i]
        position = i
    
        while position > 0 and arr[position-1] > current_value:
            
            arr[position] = arr[position-1]
            position -= 1
        
        arr[position] = current_value


    return arr

if __name__ == "__main__":
    arr = [2,3,1]
    out = insertionSort(arr)
    print(out)