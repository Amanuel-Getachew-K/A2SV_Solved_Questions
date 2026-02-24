t = int(input())
for _ in range(t):
    s = str(input())
    n = len(s)
    s += "~"

    working = set()
    i = 0
    while i < n:
        if s[i] != s[i+1]:
            working.add(s[i])
        else:
            i += 1
        
        i += 1

    res = list(working)
    res.sort()

    print("".join(res))
