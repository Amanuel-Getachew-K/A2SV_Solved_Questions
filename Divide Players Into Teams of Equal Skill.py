class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        ans = (skill[0] * skill[-1])
        left,right = 1,len(skill) - 2

        while left < right:
            if skill[left] + skill[right] != target:
                return -1
            ans += (skill[left] * skill[right])
            left += 1
            right -= 1
        
        return ans
