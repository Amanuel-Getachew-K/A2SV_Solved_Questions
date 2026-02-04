class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        block_line = ""
        in_block = False
        for line in source:
            j = 0
            if not in_block:
                block_line = ""
            while j < len(line):
                if not in_block and j + 1 < len(line) and line[j] == "/" and line[j+1] == "*":
                    in_block = True
                    j += 2
                elif in_block and j + 1 < len(line) and line[j] == "*" and line[j+1] == "/":
                    in_block = False
                    j += 2
                elif not in_block and j + 1 < len(line) and line[j] == "/" and line[j+1] == "/":
                    break
                elif not in_block:
                    block_line += line[j]
                    j += 1
                else:
                    j += 1
            if block_line and not in_block:
                ans.append(block_line)
        return ans
            
