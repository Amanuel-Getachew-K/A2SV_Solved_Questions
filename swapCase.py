def swap_case(s):
    ans = ""
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            ans += chr(ord(s[i]) - 32)
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            ans += chr(ord(s[i]) + 32)
        else:
            ans += s[i]
            
    return ans
