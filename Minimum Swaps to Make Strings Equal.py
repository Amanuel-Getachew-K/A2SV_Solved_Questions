class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        if (s1.count("x") + s2.count("x")) % 2:
            return -1
        xy = yx = 0
        for a,b in zip(s1,s2):
            if a == "x" and b == "y":
                xy += 1
            elif a == "y" and b == "x":
                yx += 1
        count = xy // 2 + yx // 2
        if xy % 2:
            count += 2
        return count
