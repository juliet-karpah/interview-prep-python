"""
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

def lcm(text1, text2):
    """

    state: at i,j what is the longest common subsequence between textA and textB to that point
    dp[i][j] = LCS(text1[0:i], text2[0:j])
    """
    d = [[0]*(len(text1)+1) for i in range(len(text2)+1)]

    for i in range(1, len(text2)+1):
        for j in range(1, len(text1)+1):
            if text2[i-1] == text1[j-1]:
                d[i][j] = d[i-1][j-1] + 1
            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    return d[-1][-1]