# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the
# length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
#
# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
# Note: The length of path between two nodes is represented by the number of edges between them.

from TreeNode import TreeNode

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if not root:
        return 0
    d = height(root.left) + height(root.right)
    d_l = diameter(root.left)
    d_r = diameter(root.right)
    return max(d, d_l, d_r)


x = TreeNode.arr_to_binary_tree([1,2,3,4,5,None,None,None,None,6])
TreeNode.in_order_traversal_rec(x)