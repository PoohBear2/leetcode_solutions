class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        
        n = len(s)
        if n == 1:
            return 1

        last_letter_max = {c: 0 for c in "abcdefghijklmnopqrstuvwxyz"}

        best_len = 0
        for i in range(n):
            if i > 0 and (ord(s[i]) - ord(s[i - 1])) % 26 == 1:
                best_len += 1
            else:
                best_len = 1
            
            last_letter_max[s[i]] = max(last_letter_max[s[i]], best_len)
        
        return sum(last_letter_max.values())
                            

