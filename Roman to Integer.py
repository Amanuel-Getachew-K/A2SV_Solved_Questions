class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = 0
        idx = 0
        while idx < len(s):
            if idx < len(s)-1 and roman_to_integer[s[idx]] < roman_to_integer[s[idx+1]]:
                ans -= roman_to_integer[s[idx]]
            else:
                ans += roman_to_integer[s[idx]]
            idx += 1
        return ans
