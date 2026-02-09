class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        q = num // 3
        if num % 3 == 0:
            return [q-1,q,q+1]
        return []
