from collections import Counter
n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

freq_a = Counter(a)
freq_b = Counter(b)

answer = 0
for key in freq_a:
    if key in freq_b:
        answer += (freq_a[key]*freq_b[key])

print(answer)
