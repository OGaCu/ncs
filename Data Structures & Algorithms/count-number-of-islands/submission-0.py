class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS???
        

        # DFS
        colSize = len(grid[0])
        rowSize = len(grid)

        def dfs(r,c):
            grid[r][c] = '0'
            if r-1 >= 0 and grid[r-1][c] == '1':
                dfs(r-1, c)
            if r+1 < rowSize and grid[r+1][c] == '1':
                dfs(r+1,c)
            if c-1 >= 0 and grid[r][c-1] == '1':
                dfs(r, c-1)
            if c+1 < colSize and grid[r][c+1] == '1':
                dfs(r, c+1)

        count = 0
        for r in range(rowSize):
            for c in range(colSize):
                if grid[r][c] == '1':
                    #dfs to mark every touching 1 to be 0
                    dfs(r, c)
                    count += 1

        return count

        '''
        def dfs(r, c):
    # Check boundaries and if the cell is water
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0':
        return
    
    # Mark the current cell as visited
    grid[r][c] = '0'
    
    # Visit neighbors
    dfs(r + 1, c)
    dfs(r - 1, c)
    dfs(r, c + 1)
    dfs(r, c - 1)
    '''

