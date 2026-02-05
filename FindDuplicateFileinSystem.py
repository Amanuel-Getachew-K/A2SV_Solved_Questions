class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pths = []
        for path in paths:
            pths.append(path.split(" "))
        content = []
        possible_ans = []
        for path in pths:
            for k in range(1,len(path)):
                i = len(path[k])-2
                j = len(path[k])-1
                while i > -1:
                    if path[k][i] == "(":
                        content.append(path[k][i+1:j])
                        possible_ans.append(path[0] + "/" + path[k][:i])
                        break
                    i -= 1
        ans = []
        from collections import defaultdict
        seen = defaultdict(list)
        for i in range(len(content)):
            seen[content[i]].append(possible_ans[i])
        for key in seen:
            if len(seen[key]) > 1:
                ans.append(seen[key]) 
        return ans
        
