class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = dict(sorted(freq.items(),key = lambda x : x[1],reverse = True))
        ans = []
        i = 0
        for key in sorted_freq:
            ans.append(key)
            i += 1
            if i == k:
                break
        return ans
