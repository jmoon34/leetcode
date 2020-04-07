# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
# Note:
#
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.

# a A
# ab Ab aB AB
def letter_case(S):
    sol = []
    for char in S:
        if char.isalpha():
            if not sol:
                sol.append(char)
                sol.append(char.upper())
            else:
                sol.extend(sol)
                for i in range(len(sol)//2):
                    sol[i] += char
                for i in range(len(sol)//2, len(sol)):
                    sol[i] += char.upper()
        else:
            if not sol:
                sol.append(char)
            else:
                for i in range(len(sol)):
                    sol[i] += char
    return sol



print(letter_case("a1b3c"))


