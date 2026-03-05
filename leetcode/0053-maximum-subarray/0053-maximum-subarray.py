class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        @cache
        def solve(i,mustcheck):
            if i >= len(nums):
                return 0 if mustcheck else -inf

            return max(nums[i] + solve(i+1,True), 0 if mustcheck else solve(i+1,False))

        return solve(0,False)