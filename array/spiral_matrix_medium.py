# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# [1,2,3]
# [4,5,6]
# [7,8,9]
# [4,0,3]
# [1,2,3]
def spiral_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    result = []
    lim = min(m, n) // 2
    layer = 0
    while layer < lim:
        # top layer
        for j in range(layer, n-layer-1):
            result.append(matrix[layer][j])
        print(result)
        # right layer
        for i in range(layer, m-layer-1):
            result.append(matrix[i][n-layer-1])
        print(result)
        # bot layer
        for j in range(layer+1, n-layer)[::-1]:
            result.append(matrix[m-layer-1][j])
        print(result)
        # left layer
        for i in range(layer+1, m-layer)[::-1]:
            result.append(matrix[i][layer])
        print(result)
        layer += 1
    if m == n and n % 2 != 0:
        result.append(matrix[layer][layer])
    if m > n and n % 2 != 0:
        for i in range(layer, m-layer):
            result.append(matrix[i][layer])
    if n > m and m % 2 != 0:
        for j in range(layer, n-layer):
            result.append(matrix[layer][j])
    return result

# method using a generator that generates all the coordinates for spiral
def spiral_matrix_re(matrix):
    def coord(r1, r2, c1, c2):
        print(r1, r2, c1, c2)
        for c in range(c1, c2):
            yield r1, c
        for r in range(r1, r2+1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2-1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1
    if not matrix:
        return []
    result = []
    r1, r2 = 0, len(matrix)-1
    c1, c2 = 0, len(matrix[0]) - 1
    while r1 <= r2 and c1 <= c2:
        for r, c in coord(r1, r2, c1, c2):
            result.append(matrix[r][c])
        r1 += 1
        r2 -= 1
        c1 += 1
        c2 -= 1
    return result


print(spiral_matrix_re([
  [1, 2, 3],
  [5, 6, 7],
  [9, 1, 0],
  [1, 3, 2],
  [3, 2, 1],
  [1, 4, 2]

]))
