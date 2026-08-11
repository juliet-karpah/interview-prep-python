def product_array_except_self(nums, k):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    """
    product = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        product[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(len(nums)-1, -1, -1):
        product[i] *= suffix
        suffix *= nums[i]

    return product