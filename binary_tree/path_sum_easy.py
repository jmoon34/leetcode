# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values
# along the path equals the given sum.
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
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

from TreeNode import TreeNode

def path_sum_iter(root, sum):
    stack = [root]
    s = 0
    while stack:
        current = stack.pop(-1)
        print(current.val, end=" ")
        s += current.val
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

def path_sum_rec(root, sum):
    def rec(node, s):
        if not node:
            return False
        if s + node.val == sum and not node.left and not node.right:
            return True
        return rec(node.left, s + node.val) or rec(node.right, s + node.val)
    return rec(root, 0)


x = TreeNode.arr_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,None,None,None,1])
y = TreeNode.arr_to_binary_tree([1,2])
TreeNode.in_order_traversal(y)
print()
print(path_sum_iter(x, 22))