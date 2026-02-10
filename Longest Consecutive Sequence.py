class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        longest = 0
        if len(nums) == 1:
            return 1
        if nums == []:
            return 0
        start = 0
        end = 1
        while end < len(nums):
            if nums[end] - nums[end-1] != 1:
                longest = max(longest,end-start)
                start = end
            end += 1
        return max(longest,end-start)
