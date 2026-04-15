class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        robot.sort()
        factory.sort(key=lambda x: x[0])

        possible_slots = []
        for pos, limit in factory:
            for _ in range(limit):
                possible_slots.append(pos)
        
        num_robots, num_slots = len(robot), len(possible_slots)
        dp = [[float("inf") for _ in range(num_slots + 1)] for _ in range(num_robots + 1)]

        for i in range(num_slots):
            dp[0][i] = 0
        
        for r in range(1, num_robots + 1):
            for f in range(1, num_slots + 1):

                skip_factory = dp[r][f - 1]

                dist = abs(possible_slots[f - 1] - robot[r - 1])
                use_factory = dist + dp[r - 1][f - 1]

                dp[r][f] = min(skip_factory, use_factory)
        
        return dp[num_robots][num_slots]

