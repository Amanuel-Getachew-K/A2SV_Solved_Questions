class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        ans = ""
        for i in range(len(original)-1,-1,-1):
            ans += original[i]
        return ans == original
