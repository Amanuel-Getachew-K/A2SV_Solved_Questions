class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        left = 0
        result = math.sqrt(c)
        right = int(math.floor(result))
        while left <= right:
            sq_sum = pow(left,2) + pow(right,2)
            if sq_sum == c:
                return True
            elif sq_sum < c:
                left += 1
            elif sq_sum > c:
                right -= 1
        return False
