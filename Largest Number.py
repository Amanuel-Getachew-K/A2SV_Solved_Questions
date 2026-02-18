class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        def customcompare(s1,s2):
            if s1 + s2 > s2 + s1:
                return -1
            elif s1 + s2 < s2 + s1:
                return 1
            else:
                return 0
        nums.sort(key = cmp_to_key(customcompare))

        return str(int("".join(nums)))
