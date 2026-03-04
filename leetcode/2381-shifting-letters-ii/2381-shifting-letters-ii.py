class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff = [0] * (len(s) + 1)
        for l,r,d in shifts:
            if d == 1:
                diff[l] += 1
                diff[r+1] -= 1
            else:
                diff[l] -= 1
                diff[r+1] += 1

        for i in range(1,len(diff)):
            diff[i] += diff[i-1]

        answer = []
        for i in range(len(s)):
            answer.append(chr(97 + ((ord(s[i])) - 97 + diff[i]) % 26))

        return "".join(answer)

        