class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = float("inf")
        for st in strs:
            n = min(len(st),n)
        ans = ""
        ck = True
        for i in range(n):
            for j in range(1,len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    ck = False
            if ck:
                ans += strs[0][i]
            else:
                break
        return ans
