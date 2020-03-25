# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

from TreeNode import TreeNode

def bottom_up_level_order(root):
    from collections import deque
    if not root:
        return None
    q = deque()
    s = []
    q.append((root, 0))
    while q:
        node, level = q.popleft()
        s.append((node, level))
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
    print(s, level)
    solution = [[] for _ in range(level+1)]
    for node, lev in s:
        solution[lev].append((node.val))
    print(solution)
    solution.reverse()
    return solution

def bottom_up_level_order_recursion(root):
    if not root:
        return []
    from collections import deque
    q = deque()
    def recurse(node, level):
        if len(q) < level:
            q.appendleft([])
        q[-level].append(node.val)
        if node.left:
            recurse(node.left, level+1)
        if node.right:
            recurse(node.right, level+1)
    recurse(root, 1)
    return q

x = TreeNode.arr_to_binary_tree([3,9,20,None,None,15,7])
print(bottom_up_level_order_recursion(x))