# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.
#
#
#
# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation:
# The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation:
# The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

import collections

def words_formed(words, chars):
    word_map = [collections.Counter(w) for w in words]
    char_map = collections.Counter(chars)
    sol = 0
    for i, c in enumerate(word_map):
        intersection = c & char_map
        if len(words[i]) == sum(intersection.values()):
            print(intersection)
            sol += sum(intersection.values())
    return sol

def words_formed_2(words, chars):
    sol = 0
    for i in range(len(words)):
        char_counts = collections.Counter(chars)
        complete = True
        match_count = 0
        for char in words[i]:
            if char in char_counts and char_counts[char] > 0:
                char_counts[char] -= 1
                match_count += 1
            else:
                complete = False
                break
        if complete:
            sol += match_count
    return sol


print(words_formed_2(["cat","bt","hat","tree"], "atach"))
print(words_formed_2(["hello","world","leetcode"], "welldonehoneyr"))