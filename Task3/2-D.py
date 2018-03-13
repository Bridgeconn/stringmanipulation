#Takes 2 different digits as input and generates a 2-dimensional array.


row_num = int(input("Enter row="))
col_num = int(input("Enter col="))
matrix = [[0 for y in range(col_num)] for x in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        matrix[row][col] = row*col

print(matrix)