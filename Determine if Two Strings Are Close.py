class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        for key in count1:
            if key not in count2:
                return False
        freq1 = [val for val in count1.values()]
        freq2 = [val for val in count2.values()]
        freq1.sort()
        freq2.sort()
        return freq1 == freq2
