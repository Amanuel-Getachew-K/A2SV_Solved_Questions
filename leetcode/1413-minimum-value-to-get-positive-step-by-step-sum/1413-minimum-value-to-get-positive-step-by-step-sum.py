class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mn = nums[0]
        total = nums[0]
        for i in range(1,len(nums)):
            total += nums[i]
            mn = min(mn,total)

        return 1 if mn > 0 else 1 - mn