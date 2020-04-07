# Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
# 
# Example 1:
# Given tree s:
# 
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4 
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.
# Example 2:
# Given tree s:
# 
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.


def subtree_rec(s, t):
    def equals(a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and equals(a.left, b.left) and equals(a.right, b.right)
    def check_nodes(s, t):
        return s and (equals(s, t) or check_nodes(s.left, t) or check_nodes(s.right, t))
    return check_nodes(s, t)
