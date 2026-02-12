class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        swapped = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != j and (i,j) not in swapped:
                    matrix[j][i],matrix[i][j] = matrix[i][j], matrix[j][i]
                    swapped.add((j,i))
        for row in matrix:
            row.reverse()
