# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# "1432" + "21" = 1453
def add_strings(num1, num2):
    return str(int("".join(list(num1))) + int("".join(list(num2))))


# 5321 = 
def add_strings_proper(num1, num2):
    n1, n2 = 0, 0
    for i in range(len(num1)):
        digit = ord(num1[i]) - ord('0')
        n1 = 10*n1 + digit
    for i in range(len(num2)):
        digit = ord(num2[i]) - ord('0')
        n2 = 10*n2 + digit
    return str(n1 + n2)

def add_strings_really_proper(num1, num2):
    sol = ""
    carry = 0
    num1 = num1.zfill(len(num2))
    num2 = num2.zfill(len(num1))
    for i in range(len(num1))[::-1]:
        s = carry
        carry = 0
        s += (ord(num1[i]) - ord('0'))
        s += (ord(num2[i]) - ord('0'))
        if s >= 10:
            carry += 1
            s %= 10
        sol = chr(s + ord('0')) + sol
    if carry == 1:
        sol = "1" + sol
    return sol

print(add_strings_really_proper("1432", "21"))
