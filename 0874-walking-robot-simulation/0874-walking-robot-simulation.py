from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        start_x, start_y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        j = 0  
        ans = 0
        obstacles_set = set(map(tuple, obstacles))
        for command in commands:
            if command == -1:
                j = (j + 1) % 4
            elif command == -2:
                j = (j - 1) % 4
            else:
                x, y = directions[j]
                for _ in range(command):
                    if (start_x + x, start_y + y) in obstacles_set:
                        break
                    start_x += x
                    start_y += y
                    ans = max(ans, start_x**2 + start_y**2)
        
        return ans
