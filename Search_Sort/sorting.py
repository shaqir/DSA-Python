
## How to detect if given array is sorted or not 

import random
import time


def is_sorted_array(arr):
    sorted = True
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            sorted = False 
    return sorted


#is_sorted_array(temparr)    
#is_sorted_array([1,2,8,4,5]) 

## Monkey Sort

def monkey_sort(arr):
    while not is_sorted_array(arr):
        random.shuffle(arr)
        time.sleep(1)
        print("shuffled:",arr)
    print("Sorted:",arr)


#monkey_sort([5,1,0,2,3])

## Sleep Sort

# 12 24 45 5 16 9 33

def sleep_sort(arr):
    for i in range(len(arr)):
            time.sleep(arr[i])
            print("->",arr[i])


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)
    sleep_sort(arr)

#insertion_sort([10,8,4,11,7])    


def bubble_sort(arr):
    # passes are n-1
    # after every pass, last element get sorted.. and so 
    for i in range(len(arr)-1):
        for j in range(len(arr)-1 - i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print(arr)

# time complexity 2 loops so : n(n-1) = n^2 = O(n^2)
# space complexity : constant = 1 : its happening in-place in python
bubble_sort([10,18,24,11,17,65,77,12,88,19,99,1,100])    
