t = int(input())
for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    balance = 0
    good = [False]*n

    for i in range(n):
        if a[i] == '1':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            good[i] = True

    flipped = False
    possible = True

    for i in range(n-1, -1, -1):
        curr = a[i]
        if flipped:
            curr = '1' if curr == '0' else '0'

        if curr != b[i]:
            if not good[i]:
                possible = False
                break
            flipped = not flipped

    print("YES" if possible else "NO")
