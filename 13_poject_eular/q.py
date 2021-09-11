

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

def find_value_diagonally(data, nDiagonal):
    v = -1
    for row in range(len(data)):
        for col in range(len(data[0])):
           # v = (find_diagonal_value_right_left(data, row, col, nDiagonal))
            v = find_diagonal_value_left_right(data, row, col, nDiagonal)
            print('row -> ' + str(row) + ' col -> ' + str(col)+ ' == '+ str(v))


dt = [
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

find_value_diagonally(dt2, 3)
#print('-> ' + str(find_diagonal_value_right_left(dt, 2, 4, 2)))i
