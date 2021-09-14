

def find_diagonal_value_left_right(data, row, col, nDiagonal):
    total = -999999
    isColGood = False
    isRowGood = False

    #check if there are till number for diagonal from
    #coloumn 'col' indeks
    if (col + nDiagonal) <= len(data[0]):
        isColGood = True

    #check if there are still row for diagonal number
    #from 'row' index 
    if (isColGood == True) & ((row + nDiagonal) <= len(data)):
        total = 1
        for x in range(nDiagonal):
            total = total * data[row + x][col + x]
    return total
   
def find_diagonal_value_right_left(data, row, col, nDiagonal):
    total = -11111111
    isColGood = False
    isRowGood = False

    if (col-nDiagonal) >= -1 :
        isColGood = True
       # print(True)
    if (isColGood == True) & ((row + nDiagonal) <= len(data)):
        total = 1
        for x in range(nDiagonal):
            total = total * data[row + x][col - x]
    return total

#find bigget multiplication result diagonally from left to right
# example left to right
# 1 0 0 0 
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
def f_d_l_r(data, nDiagonal):
    #v = -1
    #for row in range(len(data)):
     #   for col in range(len(data[0])):
      #     # v = (find_diagonal_value_right_left(data, row, col, nDiagonal))
       #     v = find_diagonal_value_left_right(data, row, col, nDiagonal)
        #    print('row -> ' + str(row) + ' col -> ' + str(col)+ ' == '+ str(v))

    temp = 0
    total = 0
    lgc = len(data[0])
    lgr = len(data)

    for row in range(lgr):
        for col in range(lgc):
            total = find_diagonal_value_left_right(data, row, col, nDiagonal)
            #print(total)
            if total > temp:
                temp = total
                total = 0
    return temp

#find the biggest multiplication result diagonnaly from right to left
# example
# 0 0 0 1
# 0 0 1 0
# 0 1 0 0
# 1 0 0 0
def f_d_r_l(data, nDiagonal):
    temp = 0
    total = 0
    lgc = len(data[0])
    lgr = len(data)

    for row in range(lgc):
        for col in range(lgr):
            total = find_diagonal_value_right_left(data, row, col, nDiagonal)
            if total > temp:
                temp = total
                total = 0
    return temp

def find_value_horizontally(data, row, col, nDiagonal):
    total = -2222222
    isColGood = False
    lgc = len(data[0])
    lgr = len(data)

    if (col + nDiagonal) <= lgc:
        total = 1
        for x in range(nDiagonal):
            total = total * data[row][col + x]
    return total

def find_value_vertically(data, row, col, nDiagonal):
    total = -8888888
    lgc = len(data[0])
    lgr = len(data)

    if (row + nDiagonal) <= lgr:
        total = 1
        for x in range(nDiagonal):
            total = total * data[row + x][col]
    return total

# find the bigget multiplication result value vertically
def f_v(data, nNumber):
    tempBe = 0
    tempAf = 0
    total = 1
    lgc = len(data[0])
    lgr = len(data)
    for row in range(lgr):
        for col in range(lgc):
            total = find_value_vertically(data, row, col, nNumber)
            if total > tempBe:
                tempBe = total
                total = 0
    return tempBe

# find the biggest multiplication result value horizontally
def f_h(data, nNumber):
    tempBe = 0
    total = 1
    lgc = len(data[0])
    lgr = len(data)

    for row in range(lgr):
        for col in range(lgc):
            total = find_value_horizontally(data, row, col, nNumber)
            if total > tempBe:
                tempBe = total
                total = 0
    return tempBe

dt= [
        [1,   2,  3,  4, 90], 
        [5,   6,  7,  8, 91],
        [9,  10, 11, 12, 92],
        [13, 14, 15, 16, 92]
    ]
dt2 = [
        [0, 1, 9, 1, 0],
        [3, 0, 0, 1, 1],
        [9, 7, 2, 1, 9],
        [3, 4, 6, 1, 9]
    ]

dt3 = [
	[ 8,  2, 22, 97, 38, 15,  0, 40,  0, 75,  4,  5,  7, 78, 52, 12, 50, 77, 91,  8], 
	[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48,  4, 56, 62,  0], 
	[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30,  3, 49, 13, 36, 65], 
	[52, 70, 95, 23,  4, 60, 11, 42, 69, 24, 68, 56,  1, 32, 56, 71, 37,  2, 36, 91], 
	[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], 
	[24, 47, 32, 60, 99,  3, 45,  2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], 
	[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], 
	[67, 26, 20, 68,  2, 62, 12, 20, 95, 63, 94, 39, 63,  8, 40, 91, 66, 49, 94, 21], 
	[24, 55, 58,  5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72], 
	[21, 36, 23,  9, 75,  0, 76, 44, 20, 45, 35, 14,  0, 61, 33, 97, 34, 31, 33, 95], 
	[78, 17, 53, 28, 22, 75, 31, 67, 15, 94,  3, 80,  4, 62, 16, 14,  9, 53, 56, 92], 
	[16, 39,  5, 42, 96, 35, 31, 47, 55, 58, 88, 24,  0, 17, 54, 24, 36, 29, 85, 57], 
	[86, 56,  0, 48, 35, 71, 89,  7,  5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58], 
	[19, 80, 81, 68,  5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,  4, 89, 55, 40], 
	[ 4, 52,  8, 83, 97, 35, 99, 16,  7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], 
	[88, 36, 68, 87, 57, 62, 20, 72,  3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69], 
	[ 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18,  8, 46, 29, 32, 40, 62, 76, 36], 
	[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74,  4, 36, 16], 
	[20, 73, 35, 29, 78, 31, 90,  1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57,  5, 54], 
	[ 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52,  1, 89, 19, 67, 48]
]

def main():
    n = 4
    d = dt3
    #total_horizontal
    t_h = f_h(d, n) 
    #total_vertical
    t_v = f_v(d, n)
    #total_diagonal_left_right
    t_d_l_r= f_d_l_r(d, n)
    #total_diagonal_right_left
    t_d_r_l= f_d_r_l(d, n)
    
    main = 0
    
    if t_h >= t_v:
        main = t_h
    else:
        main = t_v

    if main <= t_d_l_r:
        main = t_d_l_r

