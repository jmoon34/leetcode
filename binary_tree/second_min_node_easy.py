# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree
# has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among
# its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.
#
# Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.
#
# If no such second minimum value exists, output -1 instead.
#
# Example 1:
#
# Input:
#     2
#    / \
#   2   5
#      / \
#     5   7
#
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
#
#
# Example 2:
#
# Input:
#     2
#    / \
#   2   2
#
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest value.

from TreeNode import TreeNode

class Solution:
    second_min = -1
    flag = True
    def findSecondMinimumValue(self, root):
        if not root or not root.left:
            return -1
        first_min = root.val
        self.second_min = first_min
        def traverse(node):
            if not node:
                return
            if self.flag and node.val > first_min:
                self.second_min = node.val
                self.flag = False
            if not self.flag and node.val > first_min:
                self.second_min = min(self.second_min, node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return -1 if first_min == self.second_min else self.second_min


x = TreeNode.arr_to_binary_tree([1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1])
print(Solution().second_min_node(x))
