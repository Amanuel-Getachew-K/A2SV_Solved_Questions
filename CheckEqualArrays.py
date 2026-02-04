class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        from collections import Counter
        freqA = Counter(a)
        freqB = Counter(b)
        if len(a) != len(b):
            return False
        for key in freqA:
            if freqA[key] != freqB[key]:
                return False
        return True
