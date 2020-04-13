# Given an input string, reverse the string word by word.
#
#
#
# Example 1:
#
# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:
#
# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:
#
# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
#
#
# Note:
#
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.
#
#
# Follow up:
#
# For C programmers, try to solve it in-place in O(1) extra space.


def reverse_words(s):
    return " ".join(s.split()[::-1])


def reverse_words_longer(s):
    def reverse_section(left, right, arr):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    def trim_spaces(s):
        left, right = 0, len(s)-1
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        result = []
        while left <= right:
            if s[left] != ' ':
                result.append(s[left])
            elif result[-1] != ' ':
                result.append(s[left])
            left += 1
        return result
    def reverse_each_word(arr):
        n = len(arr)
        start = end = 0
        while start < n:
            while end < n and arr[end] != ' ':
                end += 1
            reverse_section(start, end - 1, arr)
            start = end + 1
            end += 1

    arr = trim_spaces(s)
    reverse_section(0, len(arr)-1, arr)
    reverse_each_word(arr)
    return "".join(arr)

print(reverse_words_longer("  the sky is  blue "))
