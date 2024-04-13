class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        count_zeros = 0
        n, m = len(grid), len(grid[0])
        product = 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] % 12345 == 0:
                    count_zeros += 1
                else:
                    product *= grid[i][j]
        
        for i in range(n):
            for j in range(m):
                if count_zeros > 1:
                    grid[i][j] = 0
                elif count_zeros == 1:
                    if grid[i][j] % 12345 == 0:
                        grid[i][j] = product % 12345
                    else:
                        grid[i][j] = 0
                else:
                   grid[i][j] =  (product // grid[i][j]) % 12345
        return grid