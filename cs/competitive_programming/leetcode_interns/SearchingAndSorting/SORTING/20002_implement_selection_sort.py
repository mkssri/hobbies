#!/usr/bin/python3

"""
SELECTION SORT is improvization of Bubble Sort with only one swap in one pass
Total of n-1 passes we need to do
"""

def selection_sort(arr):
    
    for fillslot in range(len(arr)-1,0,-1):
        
        print("fillslot is {}".format(fillslot))
        position_of_max = 0
        
        for location in range(1,fillslot+1):
            print("location is {}".format(location))

            if arr[location] > arr[position_of_max]:
                position_of_max = location
                
        
        temp = arr[fillslot]
        arr[fillslot] = arr[position_of_max]
        arr[position_of_max] = temp


    return arr



if __name__ == "__main__":

    arr = [5,8,3,10,1]
    out = selection_sort(arr)
    print(out)