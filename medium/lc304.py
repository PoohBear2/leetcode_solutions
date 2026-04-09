class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])

        self.matrix = matrix
        self.p_sum = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        self.p_sum[0][0] = matrix[0][0]

        for i in range(rows):
            for j in range(cols):
                
                self.p_sum[i + 1][j + 1] = matrix[i][j] + self.p_sum[i][j + 1] + self.p_sum[i + 1][j] - self.p_sum[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]
        
        return self.p_sum[row2 + 1][col2 + 1] - self.p_sum[row2 + 1][col1] - self.p_sum[row1][col2 + 1] + self.p_sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
