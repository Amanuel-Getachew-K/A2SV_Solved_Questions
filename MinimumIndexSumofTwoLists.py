class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        freq1 = {}
        freq2 = {}
        for idx, val in enumerate(list1):
            if val not in freq1:
                freq1[val] = idx
        for idx, val in enumerate(list2):
            if val not in freq2:
                freq2[val] = idx
        mn = float("inf")
        freq3 = {}
        for key in freq1:
            if key in freq2:
                freq3[key] = freq1[key] + freq2[key]
                mn = min(mn,freq3[key])
        ans = []
        for key,val in freq3.items():
            if val == mn:
                ans.append(key)
        return ans 
