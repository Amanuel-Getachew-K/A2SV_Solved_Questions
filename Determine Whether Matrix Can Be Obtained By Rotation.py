class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            swapped = set()
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i != j and (i,j) not in swapped:
                        mat[j][i],mat[i][j] = mat[i][j], mat[j][i]
                        swapped.add((j,i))
            for row in mat:
                row.reverse()
            if mat == target:
                return True
        return False
