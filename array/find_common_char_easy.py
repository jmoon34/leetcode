# Given an array A of strings made only from lowercase letters, return a list of all characters that show up
# in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but
# not 4 times, you need to include that character three times in the final answer.
#
# You may return the answer in any order.
#
# Example
# 1:
#
# Input: ["bella", "label", "roller"]
# Output: ["e", "l", "l"]
# Example
# 2:
#
# Input: ["cool", "lock", "cook"]
# Output: ["c", "o"]
#
# Note:
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] is a lowercase letter
import collections
def common_char(A):
    import collections
    c = [collections.Counter(a) for a in A]
    for e in c[1:]:
        c[0] &= e

    return [ e for e in c[0] for i in range(c[0][e]) ]


print(common_char(["bella", "label", "roller"]))

x = collections.Counter("maximum yolo unbelievable erging han dynasty master yassu dude")
print(x)

print([e for e in x for _ in range(x[e]) if not e == ' '])

