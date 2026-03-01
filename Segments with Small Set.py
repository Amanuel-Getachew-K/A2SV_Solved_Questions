from collections import defaultdict
n,k = map(int,input().split())
a = list(map(int,input().split()))

count = defaultdict(int)
left = 0
answer = 0

for right in range(n):
    if count[a[right]] == 0:
        k -= 1

    count[a[right]] += 1

    while k < 0:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            k += 1
        left += 1

    answer += right - left + 1

print(answer)
