"""
https://leetcode.com/problems/number-of-islands/description/
"""


def num_islands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """

    def dfs(grid, row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        dfs(grid, row - 1, col)
        dfs(grid, row, col + 1)
        dfs(grid, row + 1, col)
        dfs(grid, row, col - 1)

    num_rows, num_cols = len(grid), len(grid[0])
    num_island = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == '1':
                num_island += 1
                dfs(grid, i, j)
    return num_island
