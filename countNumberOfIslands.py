__author__ = 'kathan'

def island_visited(island_matrix, row, column, visited):
    near_by_row = [-1, -1, -1, 0, 0, 1, 1, 1]
    near_by_column = [-1, 0, 1, -1, 1, -1, 0, 1]

    visited[row][column] = True

    for i in range(8):
        if row + near_by_row[i] >= 0 and \
            row + near_by_row[i] < len(island_matrix[0]) and \
            column + near_by_column[i] >= 0 and \
            column + near_by_column[i] < len(island_matrix) and \
            not visited[row + near_by_row[i]][column + near_by_column[i]] and \
            island_matrix[row + near_by_row[i]][column + near_by_column[i]]:

            island_visited(island_matrix, row + near_by_row[i], column + near_by_column[i], visited)


def count_number_of_island(given_matrix):
    columns = len(given_matrix)
    rows = len(given_matrix[0])
    visited = [[False for j in range(columns)]for i in range(rows)]

    count = 0
    for i in range(rows):
        for j in range(columns):
            if not visited[i][j] and given_matrix[i][j]:
                island_visited(given_matrix, i, j, visited)
                count += 1

    return count



given_matrix = [[1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [1, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1]]
print count_number_of_island(given_matrix)
