class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        ans = 0
        partof = False
        for i in range(n):
            for j in range(m):
                side = 4
                if grid[i][j] == 1:
                    if i - 1 > -1 and grid[i-1][j] == 1:
                        side -= 1
                        partof = True
                    if j -1 > -1 and grid[i][j-1] == 1:
                        side -= 1
                        partof = True
                    if i + 1 < n and grid[i+1][j] == 1:
                        side -= 1
                        partof = True
                    if j + 1 < m and grid[i][j+1] == 1:
                        side -= 1
                        partof = True
                if partof:
                    ans += side
                    partof = False
        return ans if ans > 0 else 4
