# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]

# Example 2:
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

# a[0][0] => a[0][len(a[0])-1]
# a[0][1] => a[1][len(a[0])-1]
# a[i+l][j+l] => a[j+l][n-1-l] : top to right
# a[i][n-1-l] => a[n-1-l][n-1-i] : right to bot
# a[n-1-l][n-1-j] => a[n-1-j][l] : bot to left
# a[n-1-i][l] =>
def rotate_image(matrix):
    n = len(matrix)
    for i in range(n//2):
        layer = i
        for j in range(n-2*layer-1):
            temp = matrix[j+layer][n-1-layer] # right side is temp
            matrix[j+layer][n-1-layer] = matrix[i][j+layer] # top to right
            matrix[i][j+layer] = matrix[n-1-j-layer][layer] # left to top
            matrix[n-1-j-layer][layer] = matrix[n-1-layer][n-1-j-layer] # bot to left
            matrix[n-1-layer][n-1-j-layer] = temp # right to bot


x = [
  [1,2,3,4,5],
  [6,7,8,9,10],
  [11,12,13,14,15],
  [16,17,18,19,20],
  [21,22,23,24,25]
]
rotate_image(x)
print(x)



