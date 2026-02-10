t = int(input())
for _ in range(t):
    n,x,k = map(int,input().split())
    s = input().strip()
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + (1 if s[i - 1] == 'R' else -1)
    
    first_zero = -1
    for i in range(1, n + 1):
        if x + pref[i] == 0:
            first_zero = i
            break

    if first_zero == -1 or first_zero > k:
        print(0)
        continue

    k -= first_zero
    answer = 1
    cycle_len = -1
    for i in range(1, n + 1):
        if pref[i] == 0:
            cycle_len = i
            break

    if cycle_len == -1:
        print(answer)
    else:
        answer += k // cycle_len
        print(answer)
