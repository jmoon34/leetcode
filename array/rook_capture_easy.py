# On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.
# These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and
# lowercase characters represent black pieces.
#
# The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south),
# then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored
# pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.
#
# Return the number of pawns the rook can capture in one move.

# Take the rook's position as (i, j)
# Need to observe directions (i, j +-y) and (i +- x, j)
# First scan board, and while scanning, record
# {location: piece} in a dictionary
# stop scanning after finding rook and proceed to check only cardinal directions


def position():
    for i in range(8):
        for j in range(8):
            yield (i, j)

def rook(board):
    pieces = {}
    count = 0
    rook_pos = []
    for i, j in position():
            if board[i][j] == 'R':
                rook_pos = [i,j]
                break
            elif board[i][j] == 'p':
                pieces[(i,j)] = 'p'
            elif board[i][j] == 'B':
                pieces[(i,j)] = 'B'
    # Checking left covered by pieces dict
    row, col = rook_pos[0], rook_pos[1]
    while col > 0:
        col -= 1
        if (row, col) in pieces:
            if pieces[(row,col)] == 'p':
                count += 1
                break
            else:
                break
    # Checking top covered by pieces dict
    row, col = rook_pos[0], rook_pos[1]
    while row > 0:
        row -= 1
        if (row, col) in pieces:
            if pieces[(row, col)] == 'p':
                count += 1
                break
            else:
                break
    # Checking right
    row, col = rook_pos[0], rook_pos[1]
    while col < 7:
        col += 1
        if board[row][col] == 'p':
            count += 1
            break
        elif board[row][col] == 'B':
            break
    # Checking bottom
    row, col = rook_pos[0], rook_pos[1]
    while row < 7:
        row += 1
        if board[row][col] == 'p':
            count += 1
            break
        elif board[row][col] == 'B':
            break
    return count

print(rook([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","B",".",".",".","."],[".","p","B","R","p","B","p","."],[".",".",".","p","p",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))

def printer(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
printer([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","B",".",".",".","."],[".","p","B","R","p","B","p","."],[".",".",".","p","p",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]])