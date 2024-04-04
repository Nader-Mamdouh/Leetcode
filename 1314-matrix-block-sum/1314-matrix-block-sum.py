class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        answer = [[0] * n for _ in range(m)]
        cum_sum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cum_sum[i][j] = cum_sum[i - 1][j] + cum_sum[i][j - 1] - cum_sum[i - 1][j - 1] + mat[i - 1][j - 1]

        for i in range(m):
            for j in range(n):
                r1, c1 = max(0, i - k), max(0, j - k)
                r2, c2 = min(m, i + k + 1), min(n, j + k + 1)

                answer[i][j] = cum_sum[r2][c2] - cum_sum[r1][c2] - cum_sum[r2][c1] + cum_sum[r1][c1]

        return answer
        