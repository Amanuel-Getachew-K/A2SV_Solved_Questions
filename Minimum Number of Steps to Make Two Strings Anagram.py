class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqS = Counter(s)
        freqT = Counter(t)
        ans = 0
        for key in freqS:
            if freqT[key] < freqS[key]:
                ans += freqS[key]-freqT[key]
        return ans
