t = int(input())
for _ in range(t):
    n = int(input())
    permutation = list(map(int,input().split()))

    answer = []
    for i in range(n):
        if i == 0 or i == n - 1 or (permutation[i-1] < permutation[i]) != (permutation[i] < permutation[i+1]):
            answer.append(permutation[i])
            
    print(len(answer))
    print(*answer)
