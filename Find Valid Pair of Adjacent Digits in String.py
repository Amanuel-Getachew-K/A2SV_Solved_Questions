class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)
        ans = ""
        for i in range(len(s)-1):
            if s[i] != s[i+1] and freq[s[i]] == int(s[i]) and freq[s[i+1]] == int(s[i+1]):
                ans += s[i:i+2]
                break
        return ans
