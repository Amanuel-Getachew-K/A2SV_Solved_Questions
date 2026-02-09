class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for val in nums:
            if val % 2 ==0:
                even_sum += val
        ans = []
        for val,idx in queries:
            if nums[idx] % 2 == 0 and (nums[idx] + val) % 2 == 0:
                even_sum += val
            elif nums[idx] % 2 == 0 and (nums[idx] + val) % 2 != 0:
                even_sum -= nums[idx]
            elif nums[idx] % 2 != 0 and (nums[idx] + val) % 2 == 0:
                even_sum += nums[idx] + val
            ans.append(even_sum)
            nums[idx] += val
        return ans
