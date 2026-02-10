class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        freq = Counter(changed)
        changed.sort()
        ans = []
        if len(changed) % 2:
            return []
        for num in changed:
            if num == 0 and freq[num] >= 2:
                freq[num] -= 2
                ans.append(num)
            elif num > 0 and freq[num] and freq[num*2]:
                freq[num] -= 1
                freq[num * 2] -= 1
                ans.append(num)
        return ans if len(ans) == len(changed)//2 else []
