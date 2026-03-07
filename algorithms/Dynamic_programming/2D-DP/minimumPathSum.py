"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

def minimum_path_sum(grid):
    """
    state: at the current i, the minimum sum to that point
    transition: update the sum that is minimal left, top
    """
    d = [[0]* len(grid[0]) for i in range(len(grid))]

    d[0][0] = grid[0][0]

    for i in range(1, len(grid)):
        d[i][0] = grid[i][0] + d[i-1][0]

    for j in range(1, len(grid[0])):
        d[0][j] = grid[0][j] + d[0][j-1]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            d[i][j] = grid[i][j] + min(d[i-1][j], d[i][j-1])