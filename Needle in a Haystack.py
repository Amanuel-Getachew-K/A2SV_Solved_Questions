from collections import Counter
T = int(input())
for _ in range(T):
    yes = True
    s = str(input())
    t = str(input())
    freqA = Counter(s)
    freqB = Counter(t)
    for key in freqA:
        if freqB[key] < freqA[key]:
            print("Impossible")
            yes = False
            break
    if not yes:
        continue
    extra = ""
    for key in sorted(freqB):
        needed = freqB[key] -  freqA[key]
        for _ in range(needed):
            extra += key
    s += "~"
    extra += "~"
    result = ""
    p1 = p2 = 0
    while len(result) < len(t):
        if s[p1] <= extra[p2]:
            result += s[p1]
            p1 +=1
        else:
            result += extra[p2]
            p2 +=1
    print(result)
