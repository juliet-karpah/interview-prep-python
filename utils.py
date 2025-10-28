def merge(left, right):
    """
    Merge two lists in ascending order
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(right[j:])
    result.extend(left[i:])
    return result
