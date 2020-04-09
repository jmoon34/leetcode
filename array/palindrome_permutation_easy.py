# Given a string, determine if a permutation of the string could form a palindrome.
#
# Example 1:
#
# Input: "code"
# Output: false
# Example 2:
#
# Input: "aab"
# Output: true
# Example 3:
#
# Input: "carerac"
# Output: true


def palindrome_permutation(s):
    counts = {}
    odd_count = 0
    for i in range(len(s)):
        if s[i] not in counts:
            counts[s[i]] = 1
            odd_count += 1
        else:
            counts[s[i]] += 1
            if counts[s[i]] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1
    print(counts)
    return odd_count == 0 or odd_count == 1

print(palindrome_permutation("carerac"))