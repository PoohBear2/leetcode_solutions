class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        obs = set()
        for obstacle in obstacles:
            obs.add(tuple(obstacle))

        res = 0
        cur_x, cur_y = 0, 0
        dir = 0         
        """
        0 = up
        1 = right
        2 = down
        3 = left
        """

        start = True
        for command in commands:

            # Directions
            if command == -1:
                dir = (dir + 1) % 4
            
            elif command == -2:
                dir = (dir - 1) % 4

            # move
            else:
                dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                dx, dy = dirs[dir]
                nex_x, nex_y = cur_x, cur_y
                for _ in range(command):
                    nex_x += dx
                    nex_y += dy
                    if (nex_x, nex_y) in obs:
                        break
                    cur_x = nex_x
                    cur_y = nex_y
                    res = max(res, cur_x**2 + cur_y**2)
                
        return res

