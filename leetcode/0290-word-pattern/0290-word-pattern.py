class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
            
        p_to_w = {}
        w_to_p = {}
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            
            if char in p_to_w:
                if p_to_w[char] != word:
                    return False
            else:
                p_to_w[char] = word
                
            if word in w_to_p:
                if w_to_p[word] != char:
                    return False
            else:
                w_to_p[word] = char

        return True
