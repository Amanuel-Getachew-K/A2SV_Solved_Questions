n,k,q = map(int,input().split())

prefix = [0] *(200002)

for i in range(n):
    l,r = map(int,input().split())
    prefix[l] += 1
    prefix[r + 1] -= 1

for i in range(1,200002):
    prefix[i] += prefix[i-1]

count = [0] * 200002
for i in range(1,200002):
    if prefix[i] >= k:
        count[i] = 1

for i in range(1,200002):
    count[i] += count[i-1]

for _ in range(q):
    l,r = map(int,input().split())
    print(count[r] - count[l-1])