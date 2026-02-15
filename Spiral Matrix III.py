class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        ans = []
        top,left = rStart,cStart
        steps = 1
        i = 0
        while len(ans) < rows * cols:
            for _ in range(2):
                dr,dc = directions[i]
                for _ in range(steps):
                    if (0 <= top < rows) and (0 <= left < cols):
                        ans.append([top,left])
                    top += dr
                    left += dc
                i = (i + 1) % 4
            steps += 1
        return ans

                    
        

