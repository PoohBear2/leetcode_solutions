class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        r = []
        for q in queries:
            for d in dictionary:
                cnt = 0
                i = 0
                while i < len(q):
                    if d[i] != q[i]:
                        cnt += 1
                        if cnt > 2:
                            break
                    i += 1
                if cnt <= 2:
                    r.append(q)
                    break
        return r

