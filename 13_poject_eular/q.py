

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
    

dt = [
        [1,   2,  3,  4, 90], 
        [5,   6,  7,  8, 91],
        [9,  10, 11, 12, 92],
        [13, 14, 15, 16, 92]
    ]

print('-> ' + str(find_diagonal_value_left_right(dt, 1, 2, 3)))
