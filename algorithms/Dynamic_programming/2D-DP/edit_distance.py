"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
def minDistance(word1, word2):
    """
    State: minimum number of actions to convert word1[0:i] to word2[0:j]
    Transition: 
    at every step, derive the cheapest way to transform word1 to word2
    table:

      ""  r o s
    "" 0  1 2 3
    h  1
    o  2
    r  3
    s  4
    e  5
    
    insert: walking through the grid, you move right to insert word2[j-1],
    so you take the value in d[i][j-1]
    delete: you move down to delete so you remove word1[i-1], so you take 
    the value in d[i-1][j]
    replace: you move diagonally because you insert word2[j-1] and delete word1[i-1],
    so you take the value to get to d[i-1][j-1]

    you get the minimum of all there operations and add 1 to find the cost at the current point.
    """
    d = [[0] * (len(word2)+1) for i in range(len(word1)+1)]

    # when word1 is an empty string, there are j insertions
    # d[0][j-1] + 1
    for j in range(len(word2)+1):
        d[0][j] = j

    # when word2 is an empty string, there are i deletions
    # d[i-1][0] + 1
    for i in range(len(word1)+1):
        d[i][0] = i

    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1] != word2[j-1]:
                insert = d[i][j-1]
                delete = d[i-1][j]
                replace = d[i-1][j-1]
                d[i][j] = 1 + min(insert, delete, replace)
            else:
                d[i][j] = d[i-1][j-1]
    return d[-1][-1]
    