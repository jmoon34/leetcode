# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray
# scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.
# If a cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# Note:
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].

# n,m = len(M), len(M[0])
# Case 1: left edge ; condition: M[row][0] s.t. 0 <= row <= n, top left corner when row = 0, bot left corner when row = n
# Case 2: top edge ; condition: M[0][col] s.t. 0 < col < m
# Case 3: right edge ; condition: M[row][m] s.t. 0 <= row <= n, top right corner when row = 0, bot right corner when row = n
# Case 4: bot edge ; condition: M[n][col] s.t. 0 < col < m
# Case 5: inside ; condition: M[row][col] s.t. 0 < row < n, 0 < col < m

def image_smoother(M):
    n, m = len(M), len(M[0])
    S = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(n):
        for col in range(m):
            count = 0
            for adj_row in (row-1, row, row+1):
                for adj_col in (col-1, col, col+1):
                    if 0 <= adj_row < n and 0 <= adj_col < m:
                        S[row][col] += M[adj_row][adj_col]
                        count += 1
            S[row][col] //= count
    return S

def image_printer(arr):
    for i in range(len(arr)):
        print(arr[i])

x = [[1,1]]
image_printer(x)
print()
image_printer(image_smoother(x))



