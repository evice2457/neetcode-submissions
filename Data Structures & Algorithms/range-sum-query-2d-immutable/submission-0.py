import copy
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix 


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        copy_matrix = copy.deepcopy(self.matrix)
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                upper = copy_matrix[row - 1][col]
                left = copy_matrix[row][col - 1]
                cross = copy_matrix[row - 1][col -1]
                if row == row1:
                    upper = 0
                if col == col1:
                    left = 0
                if row == row1 or col == col1:
                    cross = 0
                total = copy_matrix[row][col] + upper + left - cross
                copy_matrix[row][col] = total
        return copy_matrix[row2][col2]
                


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)