class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordSet = set(wordDict)

        res = []

        def solution(cur_seq, ind):
            
            if ind >= len(s):
                res.append(" ".join(cur_seq))
                return
            
            for i in range(ind, len(s)):

                cur_word = s[ind:i+1]

                if cur_word in wordSet:

                    cur_seq.append(cur_word)
                    solution(cur_seq, i + 1)
                    cur_seq.pop()
        
        solution([], 0)
        return res

