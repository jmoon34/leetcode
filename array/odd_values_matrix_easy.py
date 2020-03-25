# Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices
# where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.
#
# Return the number of cells with odd values in the matrix after applying the increment to all indices.


def odd_value_matrix(n, m, indices):
    odd_set = set()
    for i in range(len(indices)):
        target_row = indices[i][0]
        target_col = indices[i][1]
        for col in range(m):
            if (target_row, col) not in odd_set:
                odd_set.add((target_row, col))
            else:
                odd_set.remove((target_row, col))
        for row in range(n):
            if (row, target_col) not in odd_set:
                odd_set.add((row, target_col))
            else:
                print("catch")
                odd_set.remove((row, target_col))
    return len(odd_set)

def odd_matrix_fast(n, m, indices):
    rows, cols = [0] * n, [0] * m

    for i, j in indices:
        rows[i], cols[j] = rows[i] ^ 1, cols[j] ^ 1
    return sum((r + c) % 2 for r in rows for c in cols)


print(odd_matrix_fast(2, 3, [[0,1],[1,1]]))