n = int(input())
a = list(map(int,input().split()))
a.sort()
k = 1
for num in a:
    if num < k:
        continue
    k += 1
print(k-1)
