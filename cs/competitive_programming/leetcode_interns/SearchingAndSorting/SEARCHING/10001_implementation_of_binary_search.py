#!/usr/bin/python3

# BINARY SEARCH

"""
BINARY SEARCH
Implementation of Binary Search
Iterative
Recursive
"""

"""
We can take greater advantage of the ordered list!
Instead of searching the list in sequence, a binary search will start by examining the
middle term.
"""

"""
Binary search uses Divide and Conquer!
We divide the problem in to smaller pieces, solve the smaller pieces in some way,
and then reassemble the whole problem to get the result.
"""

def binary_search(arr, ele):
    
    first = 0
    last = len(arr) -1
    found = False
    
    while(first <= last) and not found:
        
        mid = (first+last)//2
        
        if arr[mid] == ele:
            found = True
        else:
            if ele < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return found

def rec_bin_search(arr, ele):
    
    # BASE CASE
    if len(arr) == 0:
        return False
    
    # RECURSIVE CASE
    else:
        mid = len(arr)//2
        
        if arr[mid] == ele:
            return True
        else:
            
            if ele < arr[mid]:
                return rec_bin_search(arr[:mid], ele)
            else:
                return rec_bin_search(arr[mid+1:], ele)
                        
if __name__ == "__main__":
    

    arr1,ele1 = [1,2,3,4,5,6,7,8,9,10],5

    
    out1 = binary_search(arr1, ele1)
    print(out1)
    
    arr2,ele2 = [1,2,3,4,5,6,7,8,9,10],13

    
    out2 = rec_bin_search(arr2, ele2)
    print(out2)