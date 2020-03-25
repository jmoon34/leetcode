# Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. '
#    'For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.
#
# Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words
# such that f(queries[i]) < f(W), where W is a word in words.

# Example 1:
#
# Input: queries = ["cbd"], words = ["zaaaz"]
# Output: [1]
# Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

# Example 2:
#
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").

# Example 2:
#
# Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
# Output: [1,2]
# Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").


def compare_strings(queries, words):
        word_freq = sorted([w.count(min(w)) for w in words])
        print(word_freq)
        sol = []
        for query in queries:
            print(query.count(min(query)))
            sol.append(find_index(query.count(min(query)), word_freq))
        return sol

# [1, 2, 3, 3, 3, 4, 4]

def find_index(target, arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return len(arr) - (right + 1)

print(find_index(3, [1,2,3,4]))
print(compare_strings(["bbb","cc"], ["a","aa","aaa","aaaa", "aaaaa"]))



