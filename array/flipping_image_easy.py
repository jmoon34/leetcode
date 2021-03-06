# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
#
# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
#
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example,
# inverting [0, 1, 1] results in [1, 0, 0].
#
# Example 1:
#
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
# Example 2:
#
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Notes:
#
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1

x = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
y = [0 if x[i] == 1 else 1 for i in range(len(x))]
def reverse(arr):
    for i in range(len(arr)//2):
        arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]

def flip_image(A):
    sol = [[0 if A[row][col] == 1 else 1 for col in range(len(A[0]))] for row in range(len(A))]
    for i in range(len(sol)):
        for j in range(len(sol[0])//2):
            sol[i][j], sol[i][len(sol[0])-j-1] = sol[i][len(sol[0])-j-1], sol[i][j]
    return sol

print(flip_image(x))