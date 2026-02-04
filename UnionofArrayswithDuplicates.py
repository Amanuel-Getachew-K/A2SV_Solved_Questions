class Solution:    
    def findUnion(self, a, b):
        # code here
        setA = set(a)
        setB = set(b)
        return setA | setB
