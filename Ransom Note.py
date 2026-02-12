class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_r = Counter(ransomNote)
        freq_m = Counter(magazine)
        for key in freq_r:
            if freq_m[key] < freq_r[key]:
                return False
        return True
