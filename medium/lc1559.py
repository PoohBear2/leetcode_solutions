class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(x, y, px, py, element):
            visited.add((x, y))

            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == element:

                    if (nx, ny) not in visited:
                        if dfs(nx, ny, x, y, element):
                            return True
                    else:
                        if (nx, ny) != (px, py):
                            return True
            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and dfs(i, j, -1, -1, grid[i][j]):
                    return True
        return False
            

            

