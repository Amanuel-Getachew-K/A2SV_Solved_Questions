class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for key in freq:
            if freq[key] == 1:
                return key
