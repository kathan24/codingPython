__author__ = 'kathan'

def rotateMNMatrixBy90Degree(matrix, row, col):
    new_matrix = [[0 for i in range(row)] for j in range(col)]

    for i in range(row):
        for j in range(col):
            new_matrix[col - j - 1][i] = matrix[i][j]

    return new_matrix



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

#print rotateMNMatrixBy90Degree(matrix, 4, 3)





def rotateNNMatrixBy90Degree(matrix, n, rotation):
    level = 0

    while level < n/2:
        for i in range(level, n - level - 1):
            if rotation == 'anticlockwise':
                temp = matrix[level][i]
                matrix[level][i] = matrix[i][n - level - 1]
                matrix[i][n - level - 1] = matrix[n - level - 1][n - i - 1]
                matrix[n - level - 1][n - i - 1] = matrix[n - i - 1][level]
                matrix[n - i - 1][level] = temp
            else:
                temp = matrix[level][i]
                matrix[level][i] = matrix[n - i - 1][level]
                matrix[n - i - 1][level] = matrix[n - level - 1][n - i - 1]
                matrix[n - level - 1][n - i - 1] = matrix[i][n - level - 1]
                matrix[i][n - level - 1] = temp

        level += 1


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotateNNMatrixBy90Degree(matrix, 4, 'clockwise')
print matrix

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
rotateNNMatrixBy90Degree(matrix, 4, 'anticlockwise')
print matrix