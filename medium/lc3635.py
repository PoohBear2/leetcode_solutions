class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        

        n, m = len(landStartTime), len(waterStartTime)

        bestLandFirstEnd = float("inf")
        for i in range(n):
            bestLandFirstEnd = min(bestLandFirstEnd, landStartTime[i] + landDuration[i])
        
        bestWaterFirstEnd = float("inf")
        for i in range(m):
            bestWaterFirstEnd = min(bestWaterFirstEnd, waterStartTime[i] + waterDuration[i])
        
        best = float("inf")
        for i in range(n):
            cur_best = max(bestWaterFirstEnd, landStartTime[i]) + landDuration[i]
            best = min(best, cur_best)

        for i in range(m):
            cur_best = max(bestLandFirstEnd, waterStartTime[i]) + waterDuration[i]
            best = min(best, cur_best)
        
        return best
