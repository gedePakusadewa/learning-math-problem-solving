# this is the code answer for project eular no 12 questions

#1 find every trieable number from 1 to X
#2 make a factorisation function to search 5000 divisors from triable number
#3 

#lanjut implementasi https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

#implement some tips from this https://www.geeksforgeeks.org/optimization-tips-python-code/
#//lanjut ngalih mengoptimasi kodingan ne

# function to calculated and return triangle number
# from one natural number
import time

# def gt():
#     n, tmp, l, fix = 100000, 0, 0, []
#     #fix = []
#     for x in range(n):
#         tmp = tmp + (x+1)
#         # fix = delN(gf(tmp))
#         fix = gf(tmp)
#         # print(fix)
#         l = len(fix)
#         if len(fix) > 500: 
#             break
#     return l

def gt():
    n, tmp, l, fix = 40, 0, 0, []
    #fix = []
    for x in range(n):
        tmp = tmp + (x +1)
        fix = g_power(g_p(tmp))
        # print(tmp)
        if fix > 500: 
            break
    return tmp

#function to get number of divisors from one number
def gf(n):
    i, tmp = 0, []
    for x in range(n, 0, -1):
        # if x == 1 or x == n:
        #     continue
        if n%x == 0:
            # tmp.append(n/x)
            tmp.append(x)
    return tmp

# destroy any duplicate number in array
def delN(arr):
    l, tmp, tmpN, meet, fix = len(arr), arr, -1, 0, []
    #tmp = arr
    #tmpN = -1
    #meet = 0
    for x in range(0, l, 1):
        meet = 0
        tmpN = arr[x]
        for y in range(0, l, 1):
            if arr[x] == arr[y]:
                meet = meet +1
            if meet == 2:
                tmp[y] = -1
                break

    for x in tmp:
        if x == -1:
            continue
        fix.append(x)
    return fix

#get all prime factor from one number
def g_p(n):

    if n == 1:
        return 1

    prime = 2
    remain = n
    isPrime = False
    tmp = []
    div = 0
    stop = 1

    if is_p(n) == True:
        return 2

    while (stop > 0):

        if remain%prime == 0:
            tmp.append(prime)
            div = int(remain/prime)
            if is_p(div) == True:
                tmp.append(div)
                stop = 0
            if div%prime != 0:
                while (isPrime == False):
                    prime = prime + 1
                    isPrime = is_p(prime)
        isPrime = False
        remain = div
    return tmp

# check if number is prime or not
def is_p(num):
    for x in range(2, num, 1):
        if num%x == 0:
            return False
    return True

def g_power(arr):
    # print(arr)
    if arr == 1:
        return 1 

    if isinstance(arr, list) == False:
        return 2

    l = len(arr)
    tmp = {}
    for x in range(0, l, 1):
        # print(arr[x])
        if arr[x] in tmp:
            continue
        else:
            tmp.update({arr[x]:0})
            for y in range(x, l, 1):
                if arr[x] == arr[y]:
                    tmp.update({arr[x]:tmp.get(arr[x])+1}) 

    tmp2 = 1
    for x in tmp.values():
        tmp2 = tmp2 * (x+1) 
    
    return tmp2
    # print(tmp2)

def main():
    
    print(gt())

# g_power([3, 13])

# main()
for x in range(1, 11, 1):
    # print(x)
    print((g_p(x)))
# print(g_power(g_p(1)))
#a = [4,5,6,7,2,4,8,5,4]
# print(gf(12))
#gf(6)
#print(gt(11))

