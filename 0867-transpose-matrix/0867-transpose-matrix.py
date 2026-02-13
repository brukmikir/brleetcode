class Solution(object):
    def transpose(self, matrix):
        res = [[0] * len(matrix) for _ in range(len(matrix[0]))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                res[col][row] = matrix[row][col]
        return res

           
        