from collections import defaultdict
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
def group_anagram(strs):
    word_map = defaultdict(list)
    for word in strs:
        word_num = [0]*26
        for letter in word:
            num = ord(letter) - ord('a')
            word_num[num] += 1
        word_num_tuple = tuple(word_num)

        word_map[word_num_tuple].append(word)
    return list(word_map.values())