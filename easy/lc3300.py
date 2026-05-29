class Solution:
    def minElement(self, nums: List[int]) -> int:
        
        def getSum(n):
            tot = 0
            while n > 0:
                last_digit = n % 10
                tot += last_digit
                n //= 10
            return tot
        
        best = float("inf")
        for i in range(len(nums)):
            cur = getSum(nums[i])
            best = min(best, cur)
        
        return best


