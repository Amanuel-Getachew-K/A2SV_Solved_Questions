class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = len(nums)/3
        freq = Counter(nums)
        ans = []
        for key in freq:
            if freq[key] > k:
                ans.append(key)
        return ans
