# this is the code answer for project eular no 12 questions

#1 find every trieable number from 1 to X
#2 make a factorisation function to search 5000 divisors from triable number
#3 

//lanjut benerin delN(), alih adi list.remove sink nyak berfungsi???

# function to calculated and return triangle number
# from one natural number
def gt(n):
    tmp = 0
    for x in range(n):
        tmp = tmp + (x+1)
    return tmp

#function to get sum of divisors from one number
def gf(n):
    i = 0
    tmp = [1, n]
    for x in range(n, 0, -1):
        if x == 1 or x == 6:
            continue
        if n%x == 0:
            tmp.append(n/x)
            tmp.append(x)
    print(tmp)

# destroy any duplicate number in array
def delN(arr):
    l = len(arr)
    tmp = arr
    tmpN = -1
    meet = 0
    incre = 0
    for x in range(0, l, 1):
        meet = 0
        tmpN = arr[x]
        for y in range(0, l, 1):
            if arr[x] == arr[y]:
                meet = meet +1
            if meet == 2:
                tmp[y] = -1
                incre = incre + 1
                break
    #fix = tmp
    #for x in range(0, incre, 1):
    tmp.remove(-1)

    return tmp


a = [4,5,6,7,2,4,8,5,4]
print(delN(a))
#gf(6)
#print(gt(11))

