"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""

def unique_paths(m,n):
        """
        state: d[r][c] the number of ways to get to (r,c)
        transition:
        to get to d[r][c], you will need come from (r,c-1) or (r-1, c)
        """
        
        d = [[0]*(n+1) for i in range(m+1)]
        for i in range(m):
            d[i][0] = 1

        for j in range(n):
            d[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]

        return d[m-1][n-1]