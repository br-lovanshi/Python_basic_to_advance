def find_value(matrix, target):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == target:
                return [row, col]
    return [-1, -1]


class Matrix:

    def mat(self):
        row = 3
        col = 4
        value = 1
        matrix = [[0] * col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                matrix[r][c] = value
                value += 1
        return matrix


mat = Matrix()
matrix = mat.mat()
print(matrix)
print(find_value(matrix, 4))
