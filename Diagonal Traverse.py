class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row,col = len(mat),len(mat[0])
        res = []

        i,j = 0,0
        while len(res) < row * col:
            while i > -1 and j < col:
                res.append(mat[i][j])
                i -= 1
                j += 1
            i += 1
            if j >= col:
                j -= 1
                i += 1
            if len(res) == row * col:
                break
            while i < row and j > -1:
                res.append(mat[i][j])
                i += 1
                j -= 1
            j += 1
            if i >= row:
                i -=1
                j += 1
        #res.reverse()
        return res
