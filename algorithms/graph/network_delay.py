"""
https://leetcode.com/problems/network-delay-time/description/
"""
import heapq


def network_delay_time(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """
    """
    """
    distances = {i + 1: float('inf') for i in range(n)}

    distances[k] = 0

    graph = {}

    for node, t, w in times:
        if node in graph:
            graph[node][t] = w
        else:
            graph[node] = {t: w}

    visit = [(k, 0)]
    while visit:
        vertex, dist = heapq.heappop(visit)
        if dist > distances[vertex]:
            continue
        if vertex in graph:
            for target, weight in graph[vertex].items():
                new_distance = weight + dist
                if new_distance < distances[target]:
                    distances[target] = new_distance
                    heapq.heappush(visit, (target, new_distance))

    distance = list(distances.values())
    return -1 if float('inf') in distance else max(distance)
