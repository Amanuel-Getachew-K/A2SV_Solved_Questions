class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        freq = Counter(chars)
        total = 0
        for string in words:
            yes = False
            freq2 = Counter(string)
            for key in freq2:
                if key not in freq or freq2[key] > freq[key]:
                    yes = True
                    break
            if not yes:
                total += len(string)
        return total
