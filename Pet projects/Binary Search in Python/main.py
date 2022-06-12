def binary_search(arr, x, low, high):
    
    while low <= high:
    
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            low = mid - 1
        else:
            return mid
        
    return -1


array_ = [2, 3, 5, 10, 40]
x = 5
result = binary_search(array_, x, 0, len(array_)-1)

if result != -1:
    print('element under index ' + str(result))
else:
    print('not found')
    