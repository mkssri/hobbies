#!/usr/bin/python3

"""
UN-ORDERED LIST ANALYSIS

CASE                    BEST_CASE       WORST_CASE      AVERAGE_CASE
Item is present         1               n               n/2
Item is not present     n               n               n


ORDERED LIST ANALYSIS

CASE                    BEST_CASE       WORST_CASE      AVERAGE_CASE
Item is present         1               n               n/2
Item is not present     1               n               n/2
"""

# UN-Ordered LIST
def seq_search(arr, ele):
    
    pos = 0
    found = False
    
    while pos < len(arr) and not found:
        
        if arr[pos] == ele:
            found = True
        else:
            pos += 1
    return found

def ordered_seq_search(arr, ele):
    """
    Input array must be ordered/sorted!
    """
    pos = 0
    found = False
    stopped = False
    
    while pos < len(arr) and not found and not stopped:
        
        if arr[pos] == ele:
            found = True
        else:
            
            if arr[pos] > ele:
                stopped = True
            else:
                pos += 1
    return found

if __name__ == "__main__":
    
    arr,ele = [1,2,3,4,5],4

    arr1,ele1 = [1,2,3,4,5,6,7,8,9,10],4

    
    out = seq_search(arr, ele)
    print(out)
    
    out1 = ordered_seq_search(arr1, ele1)
    print(out1)