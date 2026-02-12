# Variable-Size Sliding Window

def longest_substring_without_repeating(s):
    """
    Given a string, find the length of the longest substring without repeating characters.
    """
    start = 0
    max_length = 0
    char_dict = {}

    for idx in range(len(s)):
        curr = s[idx]
        if curr in char_dict:
            start = max(start, char_dict[start] + 1)
        char_dict[curr] = idx
        max_length = max(max_length, idx - start + 1)

    return max_length
