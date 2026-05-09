class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        arr = []
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] % x != grid[0][0] % x:
                    return -1
                arr.append(grid[i][j])
        
        arr.sort()
        med = arr[(len(arr) - 1) // 2]
        res = 0
        for i in range(len(arr)):
            res += abs(med - arr[i]) // x
        return res

