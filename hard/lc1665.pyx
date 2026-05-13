class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        n = len(tasks)
        if n == 1:
            return tasks[0][1]
        
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        needed_initial = 0
        cur_amt = 0
        for actual, minimum in tasks:

            if cur_amt < minimum:
                dif = minimum - cur_amt
                cur_amt += dif
                needed_initial += dif

            cur_amt -= actual
        
        return needed_initial
        
