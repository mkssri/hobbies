#!/usr/bin/python3


def bubble_sort(arr):
    
    for n in range(len(arr)-1,0,-1):
        print("This is the n {}".format(n))
        for k in range(n):
            print("This is the k {}".format(k))

            if arr[k] > arr[k+1]:
                temp = arr[k]
                arr[k] = arr[k+1]
                arr[k+1] = temp
    
    return arr
    




if __name__ == "__main__":
    
    arr = [5,3,7,2]
    out = bubble_sort(arr)
    print(out)
    