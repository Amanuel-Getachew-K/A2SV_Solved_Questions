t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    op = []
    for i in range(n):
        for j in range(1,n):
            if a[j-1] > a[j]:
                a[j],a[j-1] = a[j-1],a[j]
                op.append([1,j])
    for i in range(n):
        for j in range(1,n):
            if b[j-1] > b[j]:
                b[j],b[j-1] = b[j-1],b[j]
                op.append([2,j])
    for i in range(n):
        if a[i] > b[i]:
            a[i],b[i] = b[i],a[i]
            op.append([3,i+1])

    print(len(op))
    for operation in op:
        print(*operation)
