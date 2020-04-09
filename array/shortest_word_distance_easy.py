# Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.

# [a,a,b,b,a,a,a,c,b,b]


# All we have to do is make one pass and update i1, i2 to point to the most recent index of word1 and word2
# and calculate the distance and compare it to min_distance
# O(n) time since it's one pass.  O(1) space since we only use two pointers to keep track of the indices
def shortest_word_distance(words, word1, word2):
    i1, i2, = -1, -1
    min_distance = float('inf')
    for i in range(len(words)):
        if words[i] == word1:
            i1 = i
        if words[i] == word2:
            i2 = i
        if i1 != -1 and i2 != 1:
            min_distance = min(min_distance, abs(i1-i2))
    return min_distance


print(shortest_word_distance(['a','a','b','b','a','a','a','c','b','b'], 'a', 'b'))
