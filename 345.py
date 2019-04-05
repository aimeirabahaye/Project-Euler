file = open("345.txt").readlines()
numberOfRows = 5
matrix = []

for i in range(numberOfRows):
    currentRow = file[i]
    matrix.append([int(a) for a in currentRow.split()]) #[row][column]


print max(matrix[0])