from collections import defaultdict
n,k = map(int,input().split())
a = list(map(int,input().split()))

count = defaultdict(int)
left = 0
longest = 0
l = r = 0

for right in range(n):
    if count[a[right]] == 0:
        k -= 1
    count[a[right]] += 1

    while k < 0:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            k += 1
        left += 1

    if right - left + 1 > longest:
        longest = right - left + 1
        l,r = left + 1,right + 1

print(l,r)
