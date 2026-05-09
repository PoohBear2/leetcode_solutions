import collections
from collections import deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return 0
        
        max_num = max(nums)
        primes = [i for i in range(max_num + 1)]

        for i in range(2, max_num + 1):
            if primes[i] == i:
                for j in range(i * i, max_num + 1, i):
                    if primes[j] == j:
                        primes[j] = i
        
        teleport_options = collections.defaultdict(list)
        
        for i, val in enumerate(nums):
            seen = set()
            temp = val

            while temp >= 2:
                
                p = primes[temp]

                if p not in seen:
                    teleport_options[p].append(i)
                    seen.add(p)

                temp //= p
        
        queue = deque([0])
        visited = {0}
        res = 0

        while queue:
            for _ in range(len(queue)):
                cur_index = queue.popleft()

                if cur_index == n - 1:
                    return res
                
                for nxt_idx in [cur_index - 1, cur_index + 1]:
                    if 0 <= nxt_idx < n and nxt_idx not in visited:
                        visited.add(nxt_idx)
                        queue.append(nxt_idx)
                
                if nums[cur_index] > 1 and primes[nums[cur_index]] == nums[cur_index]:
                    for nxt_idx in teleport_options[nums[cur_index]]:
                        if nxt_idx not in visited:
                            visited.add(nxt_idx)
                            queue.append(nxt_idx)
                    
                    del teleport_options[nums[cur_index]]

            res += 1
        
        return res

