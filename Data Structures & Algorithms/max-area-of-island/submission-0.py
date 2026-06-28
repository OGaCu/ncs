class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rowSize, colSize = len(grid), len(grid[0])
        
        def dfs(r, c) -> int:
            # out of bound check
            if r < 0 or c < 0 or r >= rowSize or c >= colSize: 
                return 0
        
            if grid[r][c] == 1:
                grid[r][c] = 0 # mark grid as visited
                return 1 + dfs(r+1, c) + dfs(r-1, c) +dfs(r, c+1) + dfs(r, c-1)
            else: # when the grid is 0 for water
                return 0

        for r in range(rowSize):
            for c in range(colSize):
                if grid[r][c] == 1:
                    curr = dfs(r, c)
                    maxArea = max(maxArea, curr)

        return maxArea