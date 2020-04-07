# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# Using recursion
def min_depth(root):
    if not root:
        return 0
    if not root.left or not root.right:
        return 1 + min_depth(root.left) + min_depth(root.right)
    return 1 + min(min_depth(root.left), min_depth(root.right))

# Using bfs.  The depth at which we find the first leaf is the minimum depth
def min_depth_bfs(root):
    from collections import deque
    if not root:
        return 0
    q = deque()
    q.append(root)
    depth = 1
    while q:
        next_level = []
        for i in range(len(q)):
            current = q.popleft()
            if not current.left and not current.right:
                return depth
            if current.left:
                next_level.append(current.left)
            if current.right:
                next_level.append(current.right)
        q.extend(next_level)
        depth += 1


# translation of the recursive solution to iterative using a stack
def min_depth_dfs(root):
    if not root:
        return 0
    min_depth = float('inf')
    stack = [(root, 1)]
    while stack:
        current, depth = stack.pop()
        if not current.left and not current.right:
            min_depth = min(min_depth, depth)
        if current.left:
            stack.append((current.left, depth + 1))
        if current.right:
            stack.append((current.right, depth + 1))
    return min_depth