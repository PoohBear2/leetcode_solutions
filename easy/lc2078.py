class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n = len(colors)
        best = 0
        for i in range(n - 1, 0, -1):
            if colors[0] != colors[i]:
                best = max(best, i)
                break
        
        for i in range(n):
            if colors[n - 1] != colors[i]:
                best = max(best, n - 1 - i)
                break
        
        return best
