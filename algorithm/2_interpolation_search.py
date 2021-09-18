#implementing simple interpolation search problem using simple array data 

def bs(arr, dt):
    
    l, mid, low, high, stop = len(arr), 0, 1, len(arr), False

    if (dt > arr[l-1]) or (dt < arr[0]):
        return -99999999999
    if arr[0] == dt:
        return 0
    if arr[l-1] == dt:
        return l-1

    #mid = 0
    #low = mid + 1
    #high = length
    #stop = False
    while stop == False:
        mid = int( ( low + (high - low) / (arr[high-1]-arr[low-1]) * (dt-arr[low-1]) ) )
        print((arr[high-1]-arr[low-1]) * (dt-arr[low-1]))

        if arr[mid - 1] < dt:
            low = mid + 1

        if arr[mid - 1] > dt:
            high = mid
            low = mid - (mid - 1)

        if arr[mid - 1] == dt:
            stop = True
        if low + 1 > high:
            stop = True
            mid = -99999999
    return mid-1
    #  0   1   2   3   4   5   6   7   8   9  10
dt = [10, 14, 19, 26, 27, 29, 31, 33, 35, 42, 44]

print(bs(dt, 35))


