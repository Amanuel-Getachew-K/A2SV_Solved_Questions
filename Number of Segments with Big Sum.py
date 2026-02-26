n,s = map(int,input().split())
a = list(map(int,input().split()))

left = total = count = 0
for right in range(n):
    total += a[right]

    while total >= s:
        count += (len(a) - right)
        total -= a[left]
        left += 1

print(count)
