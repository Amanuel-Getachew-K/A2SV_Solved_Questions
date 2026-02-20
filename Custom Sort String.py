class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq1 = Counter(order)
        freq2 = Counter(s)
        answer = ""
        
        for c in order:
            if c in freq2:
                answer += c * freq2[c]

        temp = []
        for c in s:
            if c not in freq1:
                temp.append(c)

        temp.sort()
        return answer + "".join(temp)
