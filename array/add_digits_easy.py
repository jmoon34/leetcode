# Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
#
# Example:
#
# Input: 38
# Output: 2
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
#              Since 2 has only one digit, return it.
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?

def sum_digits(num):
    sum = 0
    while num % 10 != num:
        sum += num % 10
        num //= 10
    return sum + num


def add_digits_1(num):
    dig_sum = sum_digits(num)
    while dig_sum % 10 != dig_sum:
        dig_sum = sum_digits(dig_sum)
    return dig_sum

def add_digits_2(num):
    sum_dig =  sum([int(x) for x in str(num)])
    if sum_dig < 10:
        return sum_dig
    else:
        return add_digits_2(sum_dig)

def add_digits_fast(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

for i in range(1000):
    print(i % 9, sum_digits(i) % 9)