class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednums = sorted(nums)
        ans = []
        for num in nums:
            ans.append(bisect_left(sortednums,num))
        return ans
