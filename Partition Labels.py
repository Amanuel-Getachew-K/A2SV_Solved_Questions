class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        j = maxlen = 0
        ans = []
        for i in range(len(s)):
            maxlen = max(maxlen,last[s[i]])
            if i == maxlen:
                ans.append(i-j+1)
                j = i + 1
        return ans
        
