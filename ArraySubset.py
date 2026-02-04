class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        from collections import Counter
        freqA = Counter(a)
        freqB = Counter(b)
        if len(a) < len(b):
            return False
        for key in freqB:
            if freqB[key] > freqA[key]:
                return False
        return True
