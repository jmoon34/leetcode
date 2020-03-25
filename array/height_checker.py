# Students are asked to stand in non-decreasing order of heights for an annual photo.
#
# Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
#
# Notice that when a group of students is selected they can reorder in any possible way between themselves and the non selected students remain on their seats.
#
#
#
# Example 1:
#
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# Current array : [1,1,4,2,1,3]
# Target array  : [1,1,1,2,3,4]
# On index 2 (0-based) we have 4 vs 1 so we have to move this student.
# On index 4 (0-based) we have 1 vs 3 so we have to move this student.
# On index 5 (0-based) we have 3 vs 4 so we have to move this student.
# Example 2:
#
# Input: heights = [5,1,2,3,4]
# Output: 5
# Example 3:
#
# Input: heights = [1,2,3,4,5]
# Output: 0
#
#
# Constraints:
#
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100

# [5,1,2,3,4] => [1,5,2,3,4] => [1,2,5,3,4] => [1,2,3,5,4] => [1,2,3,4,5]
# [5,1] [2,3,4]
# [5][1] [2][3,4]
# [1,5] [2,3,4]

class solution:
    count = 0
    def get_count(self, heights):
        self.merge_sort(heights)
        return self.count

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        print(left, right)
        return self.combine(left, right)

    def combine(self, left, right):
        i, j = 0, 0
        arr = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1
                self.count += 1
        while i < len(left):
            arr.append(left[i])
            i += 1
        while j < len(right):
            arr.append(right[j])
            j += 1
        return arr

s = solution()
print(s.get_count([1,1,4,2,1,3]))

