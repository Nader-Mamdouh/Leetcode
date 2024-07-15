class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        queue = deque([('0000', 0)])  
        visited = set('0000')
        
        while queue:
            key, moves = queue.popleft()
            
            if key == target:
                return moves
            
            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(key[i]) + delta) % 10
                    new_key = (
                        key[:i] + str(new_digit) + key[i+1:]
                    )
                    
                    if new_key not in visited and new_key not in deadends:
                        visited.add(new_key)
                        queue.append((new_key, moves + 1))
        
        return -1