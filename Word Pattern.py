class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = list(s.split(" "))
        if len(words) != len(pattern):
            return False
        freq = defaultdict(int)
        freq2 = defaultdict(int)
        for i in range(len(pattern)):
            if pattern[i] in freq and freq[pattern[i]] != words[i] or words[i] in freq2 and freq2[words[i]] != pattern[i]:
                return False
            freq[pattern[i]] = words[i]
            freq2[words[i]] = pattern[i]
        return True
