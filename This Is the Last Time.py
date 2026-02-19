t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    casino = [list(map(int,input().split())) for _ in range(n)]
    casino.sort(key = lambda x : x[2])
    for l,r,real in casino:
        if l <= k <= r:
            k = max(real,k)
    print(k)
