# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.


def combinations_phone_number(digits):
    from collections import defaultdict
    m = defaultdict()
    for i in range(2, 7):
        m[str(i)] = [chr(3*(i-2) + ord('a') + j) for j in range(3)]
    m['7'] = ['p','q','r','s']
    m['8'] = ['t','u','v']
    m['9'] = ['w','x','y','z']

    def back_track(start=0, seq="", i=0):
        print(seq)
        if len(seq) == len(digits):
            sol.append(seq)
            return
        for j in range(len(m[digits[i]])):
            back_track(j, seq + m[digits[i]][j], i+1)
    sol = []
    back_track()
    return sol

print(combinations_phone_number('2352'))
