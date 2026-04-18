class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        t_sum = sum(nums)

        if abs(target) > t_sum or (target + t_sum) % 2 != 0:
            return 0
        
        target_sum = (t_sum + target) // 2

        dp = [0] * (target_sum + 1)
        dp[0] = 1
    
        for n in nums:

            for i in range(target_sum, n - 1, -1):

                dp[i] += dp[i - n]
        
        return dp[target_sum]

