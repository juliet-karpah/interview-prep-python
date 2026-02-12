# Fixed-Size Sliding Window

def find_max_average(nums, k):
    """
    Given an integer array nums, find a contiguous subarray whose length
    is 'k' with the maximum/minimum average value.
    Also, output the maximum/minimum average value.

    """
    max_avg = float('-inf')
    current_sum = 0.0
    start = 0
    for idx in range(len(nums)):
        current_sum += nums[idx]
        if idx >= k - 1:
            max_avg = max(max_avg, current_sum / k)
            current_sum -= nums[start]
            start += 1

    return max_avg



