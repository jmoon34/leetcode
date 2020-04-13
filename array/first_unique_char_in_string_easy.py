# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


def first_unique_char(s):
    m = {}
    for i in range(len(s)):
        if s[i] not in m:
            m[s[i]] = i
        else:
            m[s[i]] = float('inf')
    min_index = float('inf')
    for char in m:
        if m[char] != float('inf'):
            min_index = min(min_index, m[char])
    return -1 if min_index == float('inf') else min_index


def first_unique_counter(s):
    from collections import Counter
    c = Counter(s)
    for i in range(len(s)):
        if c[s[i]] == 1:
            return i
    return -1



print(first_unique_char_bit('loveleetcode'))