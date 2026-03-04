t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    b = list(map(int,input().split()))

    prefix_a = [0] * n
    prefix_a[0] = a[0]
    for i in range(1,n):
        prefix_a[i] += prefix_a[i-1] + a[i]
    
    prefix_b = [0] * m
    prefix_b[0] = b[0]
    for i in range(1,m):
        prefix_b[i] += prefix_b[i-1] + b[i]
 
    max_ = max(0,max(prefix_a)) + max(0,max(prefix_b))

    print(max_)