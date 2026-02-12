"""
https://leetcode.com/problems/rotting-oranges/
"""


def oranges_rotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    """
    if a node is rotten,
    visit its children
    if it is not rotten, increase fresh oranges list
    """
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    queue = []
    rows, cols = len(grid), len(grid[0])
    f_or = 0
    m = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append([i, j])
            elif grid[i][j] == 1:
                f_or += 1
    while queue:
        if f_or == 0:
            return m
        m += 1
        for _ in range(len(queue)):
            cd = queue.pop(0)
            i = cd[0]
            j = cd[1]
            for d in directions:
                x, y = i + d[0], j + d[1]
                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    grid[x][y] = 2
                    queue.append([x, y])
                    f_or -= 1
    return m if f_or == 0 else -1
