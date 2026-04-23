class Solution:
    def countArrangement(self, n: int) -> int:
        
        res = 0
        def backtrack(idx, used):
            nonlocal res
            if len(used) == n:
                res += 1
                return
            
            for i in range(1, n + 1):
                if i not in used and (i % idx == 0 or idx % i == 0):
                    used.add(i)
                    backtrack(idx + 1, used)
                    used.remove(i)
        backtrack(1, set())
        return res
