import collections
from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        n = len(arr)
        if n == 1:
            if arr[0] == 0 and start == 0:
                return True
            return False
        
        if arr[start] == 0:
            return True

        adj = collections.defaultdict(list)

        for index, element in enumerate(arr):
            if index + element < n:
                adj[index].append(index + element)
            
            if index - element >= 0:
                adj[index].append(index - element)
        
        deq = deque([start])
        visited = set([start])

        while deq:
            
            deq_len = len(deq)
            for _ in range(deq_len):

                cur_index = deq.popleft()

                if arr[cur_index] == 0:
                    return True
                
                for neighbor in adj[cur_index]:
                    if neighbor not in visited:
                        deq.append(neighbor)
                        visited.add(neighbor)
        
        return False

            

