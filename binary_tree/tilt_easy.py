# Given a binary tree, return the tilt of the whole tree.
# The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and
# the sum of all right subtree node values. Null node has tilt 0.
#
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
#
# Example:
# Input:
#          1
#        /   \
#       2     3
# Output: 1
# Explanation:
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# Note:
#
# The sum of node values in any subtree won't exceed the range of 32-bit integer.
# All the tilt values won't exceed the range of 32-bit integer.

from TreeNode import TreeNode

class Solution:
    solution = 0
    def tilt_recursive(self, root):
        self.traverse(root)
        return self.solution
    def traverse(self, node):
        if not node:
            return 0
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        self.solution += abs(left - right)
        return left + right + node.val


x = TreeNode.arr_to_binary_tree([1,2,3,4,None,5])
print(Solution().tilt_recursive(x))




