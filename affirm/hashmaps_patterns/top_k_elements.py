from heapq import heappop, heappush
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
"""

def top_k_elements(nums, k):
    heap = []

    frequency_map = {}
    for i in range(len(nums)):
        frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1

    for num, freq in frequency_map.items():
        heappush(heap, (-freq, num))
    return [heappop(heap)[1] for _ in range(k)]

def top_k_elements_optimized(nums, k):
    frequency_map = {}
    for i in range(len(nums)):
        frequency_map[nums[i]] = frequency_map.get(nums[i], 0) + 1

    bucket = [[] for _ in range(len(nums)+1)]
    for num, freq in frequency_map.items():
        bucket[freq].append(num)

    result = []
    for freq in range(len(bucket)-1, 0, -1):
        for num in bucket[freq]:
            result.append(num)
            if len(result) == k:
                return result
