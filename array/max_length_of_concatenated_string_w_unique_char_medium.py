# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.
# 
# Return the maximum possible length of s.
# 
#  
# 
# Example 1:
# 
# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
# Maximum length is 4.
# Example 2:
# 
# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# Example 3:
# 
# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26
#  
# 
# Constraints:
# 
# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.

class solution:
    def max_len_unique_char(self, arr):
        arr = sorted(arr, key=lambda x: -len(x))
        lens = [0]
        for i in range(len(arr)):
            if self.no_repeats(arr[i]):
                char_set = set()
                for c in arr[i]:
                    char_set.add(c)
                for j in range(len(arr)):
                    if j != i and self.no_repeats(arr[j]):
                        if not any(s in char_set for s in arr[j]):
                            for s in arr[j]:
                                char_set.add(s)
                lens.append(len(char_set))
        return max(lens)

    def no_repeats(self, word):
        s = set()
        for c in word:
            if c in s:
                return False
            s.add(c)
        return True

print(max_len_unique_char(["cha","r","act","ers"]))

