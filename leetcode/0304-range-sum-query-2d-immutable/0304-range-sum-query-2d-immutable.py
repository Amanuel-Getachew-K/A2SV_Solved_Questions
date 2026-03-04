class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]
        for i in range(1,len(matrix) + 1):
            for j in range(1, len(matrix[0]) + 1):
                self.prefix[i][j] += self.prefix[i-1][j] + self.prefix[i][j-1] - self.prefix[i-1][j-1] + matrix[i-1][j-1]
        print(self.prefix)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1 = row1 + 1, col1 + 1
        r2,c2 =  row2 + 1, col2 + 1
        return self.prefix[r2][c2] - self.prefix[r1-1][c2] - self.prefix[r2][c1 - 1] + self.prefix[r1-1][c1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(r1,col1,r2,c2)