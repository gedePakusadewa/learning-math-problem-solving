# this is the code answer for project eular no 12 questions

#1 find every trieable number from 1 to X
#2 make a factorisation function to search 5000 divisors from triable number
#3 

//continue to test gf() function then test it then make function
// to generate dactor number 

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
    tmp = [1]

    for x in range(n, 0, -1):
        if n%x == 0:
            #tmp[i] = n/x
            #tmp[i+1] = x
            tmp.append(n/x)
            tmp.append(x)

            #i = i + 1
    print(tmp)

gf(6)
#print(gt(11))

