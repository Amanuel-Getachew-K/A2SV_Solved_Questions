class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        exist = {}
        prev = 0
        for i in range(len(nums)):
            if nums[i] % k in exist:
                return True
            
            exist[prev] = 1
            prev = nums[i] % k
        
        return False