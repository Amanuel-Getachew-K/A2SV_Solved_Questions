class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars_count = defaultdict(int) 
        left = maxLen = max_freq = 0

        for right in range(len(s)):
            chars_count[s[right]] += 1
            max_freq = max(max_freq,chars_count[s[right]])

            if right - left + 1 - max_freq > k:
                chars_count[s[left]] -= 1
                left += 1
            
            maxLen = max(maxLen,right-left+1)

        return maxLen
