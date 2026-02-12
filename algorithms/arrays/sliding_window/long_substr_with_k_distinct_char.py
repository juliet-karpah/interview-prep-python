def longest_substring_k_characters(s, k):
    """
    Given a string, find the length of the longest substring in it with no more than K distinct characters.

    Example Input and Output
    Input: s = "abcdeffg", k = 3
    Output: Length of the longest substring with at most 3 distinct characters: 4
    """
    start = 0
    max_length = 0
    char_dict = {}

    for idx in range(len(s)):
        curr_char = s[idx]
        char_dict[curr_char] = char_dict.get(curr_char, 0) + 1
        while len(char_dict) > k:
            start_char = s[start]
            char_dict[start_char] = -1
            if char_dict[start_char] == 0:
                del char_dict[start_char]
            start += 1
        max_length = max(max_length, idx - start + 1)

    return max_length
