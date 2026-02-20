class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        target = len(nums)/3
        result = []
        for key,val in freq.items():
            if val > target:
                result.append(key)
        return result
