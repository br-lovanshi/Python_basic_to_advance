def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start < len(arr):
        mid = (start + end) // 2
        if arr[mid] == target:
            print(True, mid)
            return mid
        if arr[mid] > target:
            end = mid
        else:
            start = mid
    print(False)
    return -1


class Solution:
    def create_matrix(self, row, col):
        mat = [[0] * col for _ in range(row)]
        value = 1
        for i in range(row):
            for j in range(col):
                mat[i][j] = value
                value += 1

        return mat

    """1️⃣ Search in a Sorted 2D Matrix Problem: Given an m x n matrix, where each row and column is sorted in 
    ascending order, find the target element efficiently."""

    def find_value(self, mat, target):
        for row in range(len(mat)):
            for col in range(len(mat[row])):
                if mat[row][col] == target:
                    return [row, col]

        return [-1, -1]

    def rotate(self, mat):
        n = len(mat)
        m = len(mat[n - 1])
        new_mat = [[0] * m for _ in range(n)]
        i = 0
        j = 0
        for row in range(n, 0):
            for col in range(m):
                new_mat[i][j] = mat[col][row]
                i += 1
                j += 1
        return new_mat


solution = Solution()
matrix = solution.create_matrix(3, 4)
print(matrix)
# print(solution.find_value(matrix, 5))
print(solution.rotate(matrix))
