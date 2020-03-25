# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Input: coordinates = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
# Output: false
#
# Constraints:
#
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10 ^ 4 <= coordinates[i][0], coordinates[i][1] <= 10 ^ 4
# coordinates contain no duplicate point.

# [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]

def check_straight_line(coordinates):
    base = coordinates[0]
    # Check for vertical line
    if coordinates[1][0] == base[0]:
        return coordinates[-1][0] == base[0]
    slope = (coordinates[1][1] - base[1]) / (coordinates[1][0] - base[0])
    for i in range(2, len(coordinates)):
        if (coordinates[i][1] - base[1]) / (coordinates[i][0] - base[0]) != slope:
            return False
    return True

print(check_straight_line([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))