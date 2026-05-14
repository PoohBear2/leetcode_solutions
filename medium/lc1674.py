class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        n = len(nums)
        if n == 2:
            return 0
        
        p_sums = [0 for _ in range(2 * limit + 2)]

        for i in range(n // 2):
            A = min(nums[i], nums[n - 1 - i])
            B = max(nums[i], nums[n - 1 - i])

            p_sums[2] += 2

            p_sums[A + 1] -= 1
            p_sums[A + B] -= 1

            p_sums[A + B + 1] += 1
            p_sums[B + limit + 1] += 1

        best = float("inf")
        cur = 0
        for i in range(2, 2 * limit + 1):

            cur += p_sums[i]
            best = min(best, cur)
        
        return best
