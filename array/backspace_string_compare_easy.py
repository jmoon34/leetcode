# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
#
# Example 1:
#
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# Example 2:
#
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:
#
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:
#
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:
#
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.

# "a##c" => ['a', '#', '#', 'c']
# create another arry to use as a stack
# if not #, push
# if # and not empty, pop

# return
def backspace(S, T):
    s_stack, t_stack = [], []
    s, t = list(S), list(T)
    for i in range(len(s)):
        if s[i] != '#':
            s_stack.append(s[i])
        else:
            if s_stack:
                s_stack.pop(-1)
    for i in range(len(t)):
        if t[i] != '#':
            t_stack.append(t[i])
        else:
            if t_stack:
                t_stack.pop(-1)
    return s_stack == t_stack

print(backspace('ab##', 'c#d#'))
