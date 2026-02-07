from collections import Counter


def permutation_in_string(s1, s2):
    """
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

    In other words, return true if one of s1's permutations is the substring of s2.

    Example 1
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: True
    """
    len_s1 = len(s1)
    len_s2 = len(s2)

    if len_s1 > len_s2:
        return False

    freq_s1 = Counter(s1)
    freq_s2 = Counter(s2[:len_s1])

    if freq_s1 == freq_s2:
        return True

    for i in range(len_s1, len_s2):
        # if len_s1 = 2
        # i = 2, len_s1 = 2
        # char_remove = s2[0]
        char_remove = s2[i-len_s2]
        if freq_s2[char_remove] == 1:
            del freq_s2[char_remove]
        else:
            freq_s2[char_remove] = -1

        char_add = s2[i]
        freq_s2[char_add] += 1

        if freq_s1 == freq_s2:
            return True

    return False
