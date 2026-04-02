"""
Question: Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.


Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
"""

"""
Intuition summary:
running sum and take it modulo k at each index. If the same remainder appears twice, it means the subarray between those two indices has a sum divisible by k. We store the first index where each remainder appears, and if we see it again with a distance of at least 2, we return True. We initialize {0: -1} to handle subarrays starting at index 0.
"""


def check_subarray(nums, k):
    """
    (prefix_sum[i] - prefix_sum[d]) % k == 0
    is equal to:
    prefix_sum[i] % k == prefix_sum[d] % k
    """
    prefix_sum = 0
    test = {0: -1}
    for i in range(len(nums)):
        prefix_sum += nums[i]

        remainder = prefix_sum % k

        if remainder in test:
            if i - test[remainder] >= 2:
                return True
        else:
            test[remainder] = i

    return False
