class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        connected = ""
        for num in nums:
            connected += str(num)
        ans = []
        for c in connected:
            ans.append(int(c))
        return ans
