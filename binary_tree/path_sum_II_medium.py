# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:
#
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

from TreeNode import TreeNode

# O(N) time since we have to travel at most N nodes
# O(N^2) time since we have to maintain the sums within the stack (which is proportional to N)
# If the binary tree is unbalanced, worst case for storing all the sum is proportional to N
def path_sum_iter(root, sum):
    if not root:
        return None
    solution = []
    stack = [(root, [root.val])]
    while stack:
        current, vals = stack.pop()
        if not current.left and not current.right and sum(vals) == s:
            solution.append(vals)
        if current.left:
            stack.append((current.left, vals + [current.left.val]))
        if current.right:
            stack.append((current.right, vals + [current.right.val]))
    return solution

def path_sum_rec(root, target):
    if not root:
        return None
    solution = []
    def recurse(node, s):
        s.append(node.val)
        print(s)
        if not node.left and not node.right and sum(s) == target:
            solution.append(s[:])
        if node.left:
            recurse(node.left, s)
        if node.right:
            recurse(node.right, s)
        s.pop()
    recurse(root, [])
    return solution

x = TreeNode.arr_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,None,5,1])
print(path_sum_rec(x, 22))