from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        last_seen = {}
        best = float("inf")
        for index, n in enumerate(nums):

            if n in last_seen:
                best = min(best, abs(index - last_seen[n]))
            
            n_rev = int(str(n)[::-1])
            last_seen[n_rev] = index
        
        return -1 if best == float("inf") else best

