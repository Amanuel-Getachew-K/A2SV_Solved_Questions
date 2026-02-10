class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while n not in hset:
            hset.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
            if n == 1:
                return True
        else:
            return False
