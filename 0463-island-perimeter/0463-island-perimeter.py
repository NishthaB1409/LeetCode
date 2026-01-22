class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def dfs(r, c):
            # out of bounds or water contributes 1 to perimeter
            if r < 0 or r >= n or c < 0 or c >= m or grid[r][c] == 0:
                return 1
            
            # already visited land contributes 0
            if grid[r][c] == 2:
                return 0
            
            # mark land as visited
            grid[r][c] = 2
            
            # sum all four directions
            return (
                dfs(r - 1, c) +
                dfs(r + 1, c) +
                dfs(r, c - 1) +
                dfs(r, c + 1)
            )

        # find first land cell and start DFS
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0
