#implementing simple binary search problem using simple array data 

def bs(dataArray, keywords):
    low = -999
    high = -999
    mid = -999
    length = len(dataArray)
    stop = False
    while stop == False:
        low = length - (length - 1)
        high = length
        mid = int((low + (high - low)/2)) - 1
        print(mid)
        
        if dataArray[mid] < keywords:
            low = mid + 1
        
        if dataArray[mid] > keywords:
            

        #length = mid
        
        if int(mid) == 0:
            stop = True

    return mid

dt = [10, 14, 19, 26, 27, 31, 33, 35, 42, 44]

print(bs(dt, 31))
        
