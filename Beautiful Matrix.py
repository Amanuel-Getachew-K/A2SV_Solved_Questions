one = 0
for i in range(5):
    col = list(map(int,input().split()))
    for j in range(5):
        if col[j] == 1:
            one = abs(i-2) + abs(j-2)
print(one)
