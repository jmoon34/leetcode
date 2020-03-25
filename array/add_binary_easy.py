# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

a = [1,0,1,1]

def add_binary(n, m):
    max_len = max(len(n), len(m))
    n = n.zfill(max_len)
    m = m.zfill(max_len)
    result = ""
    carryover = 0
    for i in range(-1, -max_len-1, -1):
        s = carryover
        s += 1 if n[i] == '1' else 0
        s += 1 if m[i] == '1' else 0
        result = ('1' if s % 2 == 1 else '0') + result
        carryover = 0 if s < 2 else 1
        print(result, carryover, s)
    if carryover != 0:
        result = '1' + result
    return result


print(add_binary("11", "1"))
