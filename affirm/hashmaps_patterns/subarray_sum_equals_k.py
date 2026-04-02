def subarray_sum_equals_k(nums, k):
    """
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

    

    Example 1:

    Input: nums = [1,1,1], k = 2
    Output: 2
    Example 2:

    Input: nums = [1,2,3], k = 3
    Output: 2
    """
    seen_prefix = {0: 1}
    total_sum = 0
    count = 0
    for i in range(len(nums)):
        total_sum += nums[i]
        previous_sum = total_sum - k

        if previous_sum in seen_prefix:
            count += seen_prefix[previous_sum]

        seen_prefix[total_sum] = seen_prefix.get(total_sum, 0) + 1
    return count