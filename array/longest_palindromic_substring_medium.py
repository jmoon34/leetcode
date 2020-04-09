# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


from collections import defaultdict


# This solution works in O(n^2) time since it goes through n elements and for each n element we have to
# expand left/right by at most n.  It uses O(n) time since it just uses one array to store the maximum
# length of the palindrome starting at each index.
# Note that the dynamic programming array is in fact unnecessary, and we can just keep track of the
# maximum length and the index.  This will be reflected in the method below
def longest_palindrome(s):
    dp = [1 for i in range(len(s))]
    max_len = 1
    max_index = 0
    # loop for handling single middle char
    for i in range(len(s)):
        left, right = i-1, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        dp[left+1] = right - left - 1
        if dp[left + 1] > max_len:
            max_len = dp[left + 1]
            max_index = left + 1
    # loop for handling cases with pairs
    for i in range(len(s)):
        right = i + 1
        if right < len(s) and s[right] == s[i]:
            right += 1
            left = i-1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            dp[left+1] = max(dp[left+1], right - left - 1)
            if dp[left+1] > max_len:
                max_len = dp[left+1]
                max_index = left+1
    return s[max_index:max_index+max_len]

def longest_palindrome_const_space(s):
    max_len = 1
    max_index = 0
    # loop for handling single middle char
    for i in range(len(s)):
        left, right = i-1, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if right - left - 1 > max_len:
            max_len = right - left - 1
            max_index = left + 1
    # loop for handling cases with pairs
    for i in range(len(s)):
        right = i + 1
        if right < len(s) and s[right] == s[i]:
            right += 1
            left = i-1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > max_len:
                max_len = right - left - 1
                max_index = left + 1
    return s[max_index:max_index+max_len]



print(longest_palindrome_const_space("babad"))
