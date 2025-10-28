def two_sum(nums, target):
    """
    https://leetcode.com/problems/two-sum/description/
    """
    m = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in m:
            return [i, m[nums[i]]]
        m[diff] = i
    return []