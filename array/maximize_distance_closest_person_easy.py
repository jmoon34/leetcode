# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to closest person.
#
# Example 1:
#
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:
#
# Input: [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:
#
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.


# [1,0,0,0,1,0,0,1,0,0,0,0,1]

def max_seat_away(seats):
    from_left = [0 for _ in range(len(seats))]
    from_right = [0 for _ in range(len(seats))]
    l_distance = 20001
    r_distance = 20001
    for i in range(len(seats)):
        if seats[i] == 1:
            l_distance = 0
            from_left[i] = l_distance
        else:
            l_distance += 1
            from_left[i] = l_distance
        if seats[len(seats)-i-1] == 1:
            r_distance = 0
            from_right[len(seats)-i-1] = r_distance
        else:
            r_distance += 1
            from_right[len(seats)-i-1] = r_distance

    combined = [min(x,y) for x,y in zip(from_left, from_right)]
    print(from_left)
    print(from_right)
    print(combined)
    return max(combined)

print(max_seat_away([1,0,0,0,1,0,0,1,0,0,0,0,1]))

# [0,4,7,12]