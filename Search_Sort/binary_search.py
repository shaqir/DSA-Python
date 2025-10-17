# Binary Search

# Sorted Array : Time Complexity Linear O(n)

import random
import time


def binary_search(arr,low,high,item):
    if low <= high:
        #search
        mid = (low+high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr,low, mid-1, item)
        else:
            return binary_search(arr, mid+1, high, item)
    else:
        return -1


temparr = [10,20,30,40,50,60,70]

print(binary_search(temparr,0,len(temparr)-1,60))

