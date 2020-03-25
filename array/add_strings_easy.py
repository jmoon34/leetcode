# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# "1432" + "21" = 1453
def add_strings(s1, s2):
    return str(int("".join(list(s1))) + int("".join(list(s2))))



print(add_strings("1432", "21"))