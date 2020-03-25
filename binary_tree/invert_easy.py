# Invert a binary tree.
#
# Example:
#
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


from TreeNode import TreeNode

# [4,2,7,1,3,6,9] => [4,7,2,9,6,3,1]
def invert_binary_tree_recursion(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_binary_tree_recursion(root.left)
    invert_binary_tree_recursion(root.right)
    return root

def invert_binary_tree_iter(root):
    from collections import deque
    if not root:
        return None
    q = deque()
    q.append(root)
    while q:
        current = q.popleft()
        current.left, current.right = current.right, current.left
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return root

x = TreeNode.arr_to_binary_tree([4,2,7,1,3,6,9])
TreeNode.in_order_traversal(x)
print()
x = invert_binary_tree_iter(x)
TreeNode.in_order_traversal(x)
