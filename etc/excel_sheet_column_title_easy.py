# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# Example 1:
#
# Input: 1
# Output: "A"
# Example 2:
#
# Input: 28
# Output: "AB"
# Example 3:
#
# Input: 701
# Output: "ZY"

# 28 = 1*26^1 + 2*26^0
# 701 = 26*26^1 + 25*26^0
# 52 = 1*26^1 + 26*26^0
def excel_column_title(n):
    result = ""
    while n > 0:
        n -= 1
        n, mod = divmod(n, 26)
        print("n:", n, "mod:", mod, chr(ord('A') + mod))
        result = chr(ord('A') + mod) + result
    return result

print(excel_column_title(701))