

# Brute Force
def linear_search(arr,item):

    for i in range(len(arr)):
        if arr[i] == item:
            return i
    print(-1)
        

arr = [1,2,3,4,5,6,7,8,9]
print(linear_search(arr,5))
print(linear_search(arr,10))

