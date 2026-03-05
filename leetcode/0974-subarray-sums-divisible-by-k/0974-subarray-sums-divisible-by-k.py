class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        exist = {0:1}
        total = 0
        for n in nums:
            total += n
            if total % k in exist:
                count += exist[total % k]
                exist[total % k] += 1
            else:
                exist[total % k] = 1

        return count