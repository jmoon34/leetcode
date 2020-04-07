# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
# For example, given n = 3, a solution set is:
# 
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


# n = 1
# ()
#
# n = 2
# (()), ()()

# Generate all possible permutations of parenthesis and check each for valid ones
# O(n2^(2n)) time since for each of the 2^(2n) sequences, we have to create and validate them
# O(n2^(2n)) same reason as time
class Solution:
    def generate_parentheses_rec(self, n):
        def generate(a = []):
            if len(a) == 2*n:
                if valid(a):
                    ans.append("".join(a))
            else:
                a.append('(')
                generate(a)
                a.pop()
                a.append(')')
                generate(a)
                a.pop()

        def valid(a):
            balance = 0
            for p in a:
                if p == '(':
                    balance += 1
                else:
                    balance -= 1
                if balance < 0:
                    return False
            return balance == 0
        ans = []
        generate()
        return ans


# Identical to the approach above, but with a slightly different recursive approach
def paren(n):
    def all_possible(n=n*2):
        if n == 1:
            return ["(", ")"]
        a = []
        prev = all_possible(n-1)
        for p in prev:
            a.append(p + "(")
            a.append(p + ")")
        return a

    def valid(s):
        balance = 0
        for c in s:
            if c == "(":
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
        return balance == 0

    return [x for x in all_possible() if valid(x)]


def paren_backtracking(n):
    solution = []
    def backtrack(s='', left=0, right=0):
        if len(s) == 2*n:
            solution.append(s)
            return
        if left < n:
            backtrack(s + '(', left+1, right)
        if right < left:
            backtrack(s + ')', left, right+1)
    backtrack()
    return solution

print(paren_backtracking(4))

# s = Solution()
# print(s.generate_parentheses_rec(4))

