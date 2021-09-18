# this is the code answer for project eular no 12 questions

#1 find every trieable number from 1 to X
#2 make a factorisation function to search 5000 divisors from triable number
#3 

lanjut implementasi https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

implement some tips from this https://www.geeksforgeeks.org/optimization-tips-python-code/
#//lanjut ngalih mengoptimasi kodingan ne

# function to calculated and return triangle number
# from one natural number
def gt():
    n, tmp, l, fix = 500, 0, 0, []
    #fix = []
    for x in range(n):
        tmp = tmp + (x+1)
        fix = delN(gf(tmp))
       # print(len(fix))
        l = len(fix)
        if len(fix) > 500: 
            break
    return l

#function to get sum of divisors from one number
def gf(n):
    i, tmp = 0, [1, n]
    for x in range(n, 0, -1):
        if x == 1 or x == n:
            continue
        if n%x == 0:
            tmp.append(n/x)
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

def main():
    

    print(gt())

main()
#a = [4,5,6,7,2,4,8,5,4]
#print(delN(a))
#gf(6)
#print(gt(11))

