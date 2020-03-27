# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
# also represented as a string.
#
# Example 1:
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


def multiply_strings(num1, num2):
    n1, n2 = 0, 0
    for i in range(len(num1))[::-1]:
        n1 += (10**(len(num1)-1-i))*(ord(num1[i]) - ord('0'))
        print(n1)
    for j in range(len(num2))[::-1]:
        n2 += (10**(len(num2)-1-j)*(ord(num2[j]) - ord('0')))
    return str(n1*n2)


print(multiply_strings("42", "50"))