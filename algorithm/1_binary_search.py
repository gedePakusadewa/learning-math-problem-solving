#implementing simple binary search problem using simple array data 

def bs(dataArray, keywords):
    if (keywords > dataArray[len(dataArray)-1]) or (keywords < dataArray[0]):
        return -99999999999

    length = len(dataArray)
    mid = 0
    low = mid + 1
    high = length
    stop = False
    while stop == False:
        mid = int((low + (high - low)/2))
   #     print(mid)
        
        if dataArray[mid - 1] < keywords:
            low = mid + 1
        
        if dataArray[mid - 1] > keywords:
            high = mid
            low = mid - (mid - 1)
 
        if dataArray[mid - 1] == keywords:
            stop = True
        if low + 1 > high:
            stop = True
            mid = -99999999
    return mid-1

dt = [10, 14, 19, 26, 27, 29, 31, 33, 35, 42, 44]

print(bs(dt, 28))
        
