# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.


def longest_common_prefix(strs):
    if not strs:
        return ""
    sol = ""
    s = strs[0]
    for i in range(len(s)):
        for word in strs:
            if i >= len(word) or word[i] != s[i]:
                return sol
        sol += s[i]
    return sol

print(longest_common_prefix([""]))