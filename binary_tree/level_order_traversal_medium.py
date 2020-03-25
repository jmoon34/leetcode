# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

from TreeNode import TreeNode


def level_order_traversal(root):
    if not root:
        return []
    from collections import deque
    q = deque()
    val_lev = []
    q.append((root, 0))
    while q:
        node, level = q.popleft()
        val_lev.append((node.val, level))
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    sol = [[] for i in range(level + 1)]
    for val, lev in val_lev:
        sol[lev].append(val)
    return sol


def level_order_traversal_iter_2(root):
    if not root:
        return []
    solution = []
    q = [root]
    while q:
        next_level = []
        values = []
        for node in q:
            values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        solution.append(values)
        q = next_level
    return solution





x = TreeNode.arr_to_binary_tree([3,9,20,None,2,15,7])
print(level_order_traversal_iter_2(x))



