from collections import defaultdict
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    checkered = str(input())

    if n == k:
        print(n - checkered.count("B"))
    else:
        count = defaultdict(int)
        for i in range(k):
            count[checkered[i]] += 1

        mn = count['W']
        left = 0
        for right in range(k,n):
            count[checkered[left]] -= 1
            left += 1
            count[checkered[right]] += 1

            mn = min(mn,count['W'])
        print(mn)
