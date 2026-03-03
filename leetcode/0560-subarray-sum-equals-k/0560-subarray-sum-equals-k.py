class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        exist = {0:1}
        count = 0
        for i in range(len(nums)):
            if nums[i] - k in exist:
                count += exist[nums[i] - k]
            
            exist[nums[i]] = exist.get(nums[i],0) + 1
        return count