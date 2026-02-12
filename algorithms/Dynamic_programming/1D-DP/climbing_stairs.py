"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""

def climbing_stairs(n):
    """
    Pseudocode:

    choose 1 or 2 steps

    optimal substructure: 
    if step == 1, remaining steps n-1
    if step == 2, remaining steps n-2
    
    recurrence:
    base case: 
    if n = 0, ways[0] = 1
    if n = 1, ways[1] = 1
    if n = 2, ways[2] = 2(the step from 0 + the step from 1)

    state: number of ways to get to current staircase.
    transition: each step can be reached from the previous one or two steps
    """
    T = [0] * (n+1)
    for i in range(n+1):
        if i == 0:
            T[i] = 1
        elif i == 1:
            T[i] = 1
        elif i == 2:
            T[i] = 2
        else:
            T[i] = T[i-2] + T[i-1]
    return T[n]
    




