class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = Counter(nums)
        f = x = 0
        for key,val in freq.items():
            if val > f:
                f = val
                x = key
        f1 = [0] * (len(nums) + 1)
        for i in range(1,len(f1)):
            f1[i] = f1[i-1] + 1 if nums[i-1] == x else f1[i-1]
        idx = -1
        for i in range(1,len(f1)):
            f2 = f - f1[i]
            if f1[i] > i - f1[i] and f2 > len(nums) - i - f2:
                idx = i - 1
                break
        return idx
