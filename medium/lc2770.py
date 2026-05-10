class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        
        dp = [0 for _ in range(n)]
        possible = [False for _ in range(n)]
        possible[-1] = True

        for i in range(n - 2, -1, -1):
            index_to_jump_to = -1
            best = -1
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target and possible[j]:
                    
                    if best < dp[j]:
                        best = dp[j]
                        index_to_jump_to = j

            if index_to_jump_to >= 0:
                possible[i] = True
                dp[i] = 1 + dp[index_to_jump_to]
        
        return dp[0] if dp[0] != 0 else -1

