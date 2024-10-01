
## find no. of ways to reach to the bottom right corner

class Solution:
    def minPathSum(self,grid) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n  # Initialize with a large value

        # Start from the bottom-right corner
        dp[-1] = 0

        for r in reversed(range(m)):
            for c in reversed(range(n)):
                dp[c] = grid[r][c] + min(dp[c], dp[c + 1] if c+1 <n else float("inf"))

        return dp[0]
grid = [[1,2,3],[4,5,6]]
Solution().minPathSum(grid)
