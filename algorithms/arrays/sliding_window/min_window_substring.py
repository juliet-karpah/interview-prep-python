from collections import defaultdict


def min_window_substring(s1, s2):
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s1 such that every
    character in s2 (including duplicates) is included in the window.
    If there is no such substring, return the empty string "".
    """
    s2_dict = defaultdict(int)

    for char in s2:
        s2_dict[char] += 1

    min_length = float('inf')
    start = 0
    move = 0
    min_string = ""

    total_char_count = len(s2_dict)
    window_char_count = 0

    window_char_dict = defaultdict(int)

    while move < len(s1):
        curr_char = s1[move]
        window_char_dict[curr_char] += 1

        if curr_char in s2_dict and window_char_dict[curr_char] == s2_dict[curr_char]:
            window_char_count += 1

        while start <= move and window_char_count == total_char_count:
            new_window = move - start + 1
            if new_window < min_length:
                min_length = new_window
                min_string = s1[start:move+1]

            char_remove = s1[start]
            window_char_dict[char_remove] = -1

            if char_remove in s2_dict and window_char_dict[char_remove] < s2_dict[char_remove]:
                window_char_count = -1

            start += 1
        move += 1
    return min_string
