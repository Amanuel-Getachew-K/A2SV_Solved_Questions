class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        exist = {0:1}
        total = 0
        answer = 0
        for num in nums:
            total += num
            if total % k in exist:
                answer += exist[total % k]
                exist[total % k] += 1
            else:
                exist[total % k] = 1

        return answer