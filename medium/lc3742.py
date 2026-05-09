class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:

        def get_cost(e):
            if e == 1 or e == 2:
                return 1
            return 0
        
        rows, cols = len(grid), len(grid[0])
        dp = [[[-float("inf") for _ in range(k + 1)] for _ in range(cols)] for _ in range(rows)]

        start_cost = get_cost(grid[0][0])
        if start_cost > k:
            return -1
        dp[0][0][start_cost] = grid[0][0]

        for i in range(rows):
            for j in range(cols):

                if i == 0 and j == 0:
                    continue
                cur_cost = get_cost(grid[i][j])

                for possible_c in range(cur_cost, k + 1):

                    c = possible_c - cur_cost
                    
                    score_up = dp[i - 1][j][c] if i - 1 >= 0 else -float("inf")
                    score_left = dp[i][j - 1][c] if j - 1 >= 0 else -float("inf")
                    
                    best_score = max(score_up, score_left)
                    if best_score != -float("inf"):
                        dp[i][j][possible_c] = grid[i][j] + best_score
        
        res = max(dp[-1][-1])
        return -1 if res == -float("inf") else res

                    
                    
        
