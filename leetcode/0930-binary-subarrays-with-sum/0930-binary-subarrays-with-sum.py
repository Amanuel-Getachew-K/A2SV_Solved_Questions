class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0: return 0
            total = answer = left = 0
            for right in range(len(nums)):
                total += nums[right]
                while total > goal:
                    total -= nums[left]
                    left += 1
                answer += right - left + 1
            return answer
        
        return atMost(goal) - atMost(goal - 1)
