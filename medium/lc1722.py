import collections
class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        def bfs(i):
            stack = [i]
            visited[i] = True

            unseen = collections.defaultdict(int)
            idx = []

            while stack:
                cur_node = stack.pop()
                val = source[cur_node]

                idx.append(cur_node)
                unseen[val] += 1
                
                for neighbor in adj[cur_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            d = 0
            for i in idx:
                val = target[i]
                if unseen[val] > 0:
                    unseen[val] -= 1
                else:
                    d += 1
            
            return d

        n = len(source)
        s = set(range(n))

        adj = collections.defaultdict(list)

        for a, b in allowedSwaps:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False for _ in range(n)]
        
        dist = 0
        for i in range(n):
            if not visited[i]:
                dist += bfs(i)
        return dist


