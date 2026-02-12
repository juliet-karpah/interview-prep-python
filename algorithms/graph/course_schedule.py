"""
https://leetcode.com/problems/course-schedule/description/
"""


def can_finish(num_courses, prerequisites):
    """
        :type num_courses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
    graph = {i: [] for i in range(num_courses)}

    for i, j in prerequisites:
        graph[i].append(j)

    visiting = set()
    visited = set()

    def dfs(start):
        if start in visiting:
            return True
        if start in visited:
            return False

        visiting.add(start)

        for el in graph[start]:
            if dfs(el):
                return True
        visiting.remove(start)
        visited.add(start)
        return False

    for i in range(num_courses):
        if dfs(i):
            return False
    return len(visited) == num_courses
