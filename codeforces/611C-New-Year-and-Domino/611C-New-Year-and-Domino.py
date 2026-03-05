h,w = map(int,input().split())

hor_prefix = [[0] * (w + 1) for _ in range(h+1)]
ver_prefix = [[0] * (w + 1) for _ in range(h+1)]

grid = [str(input()) for _ in range(h)]

for i in range(1,h+1):
    for j in range(1,w + 1):
        if j < w and grid[i-1][j-1] == '.' and grid[i-1][j] == '.':
            hor_prefix[i][j] = 1
        
        if i < h and grid[i-1][j-1] == '.' and grid[i][j-1] == '.':
            ver_prefix[i][j] = 1

for i in range(1,h+1):
    for j in range(1,w + 1):
        hor_prefix[i][j] += hor_prefix[i-1][j] + hor_prefix[i][j-1] - hor_prefix[i-1][j-1]
        ver_prefix[i][j] += ver_prefix[i-1][j] + ver_prefix[i][j-1] - ver_prefix[i-1][j-1]


for _ in range(int(input())):
    answer = 0
    r1,c1,r2,c2 = map(int,input().split())

    answer += hor_prefix[r2][c2-1] - hor_prefix[r1-1][c2-1] - hor_prefix[r2][c1-1] + hor_prefix[r1-1][c1-1]
    answer += ver_prefix[r2-1][c2] - ver_prefix[r1-1][c2] - ver_prefix[r2-1][c1-1] + ver_prefix[r1-1][c1-1]
    
    print(answer)