class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        sTuple = sorted(s,key = lambda x: (freq[x],x),reverse = True)
        return "".join(sTuple)
        
