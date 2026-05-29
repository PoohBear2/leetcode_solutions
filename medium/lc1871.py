from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        n = len(s)
        if s[-1] != "0":
            return False

        if n == 2:
            if not minJump <= 1:
                return False
            return True
        
        deq = deque([0])
        farthest = -1

        while deq:
            
            cur_index = deq.popleft()

            if cur_index == n - 1:
                return True
            
            start = max(farthest + 1, cur_index + minJump)
            end = min(n - 1, cur_index + maxJump)

            for i in range(start, end + 1):
                if s[i] == "0":
                    deq.append(i)
            
            farthest = max(farthest, cur_index + maxJump)
        
        return False
                


