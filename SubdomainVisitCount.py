class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        ans = defaultdict(int)
        for cp in cpdomains:
            separate = list(cp.split(" "))
            domains = list(separate[1].split("."))
            temp = domains[-1]
            ans[temp] += int(separate[0])
            for i in range(len(domains)-2,-1,-1):
                temp = domains[i] + "." + temp
                ans[temp] += int(separate[0])
        res = []
        for key in ans:
            res.append(str(ans[key]) + " " + key)
        res.reverse()
        return res
