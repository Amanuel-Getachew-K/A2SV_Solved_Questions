class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        nonduplicate_res = []
        for response in responses:
            nonduplicate_res += list(set(response))
        freq = Counter(nonduplicate_res)
        max_ = 0
        for val in freq.values():
            max_ = max(max_,val)
        res = []
        for key,val in freq.items():
            if val == max_:
                res.append(key)
        return min(res)
