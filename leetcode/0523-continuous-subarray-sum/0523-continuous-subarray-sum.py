class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        exist = {0:-1}
        total = 0
        for i,n in enumerate(nums):
            total += n
            r = total % k
            if not r in exist:
                exist[r] = i
            elif i - exist[r] > 1:
                return True
        
        return False