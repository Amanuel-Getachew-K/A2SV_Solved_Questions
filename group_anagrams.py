class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [[strs[0]]]
        count = defaultdict(list)
        ans = []
        for key in strs:
            count["".join(sorted(key))].append(key)
        for key in count:
            ans.append(count[key])
        return ans
