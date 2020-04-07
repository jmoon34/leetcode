# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---

from TreeNode import TreeNode

# bfs approach.  O(n) time since we have to go through all the nodes and O(n) space since we use a queue
# The idea is the add to the solution the value of the last node in each level
def right_side_view_bfs(root):
    if not root:
        return None
    from collections import deque
    q = deque()
    q.append(root)
    solution = []
    while q:
        nodes_in_level = len(q)
        for i in range(nodes_in_level):
            current = q.popleft()
            if i == nodes_in_level-1:
                solution.append(current)
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
    return solution

# dfs approach. O(n) time since directed acyclic graph so goes through all nodes, and O(n) space since
# use a stack.  The idea is to always pop the right child first, so the right most will always be the first
# node in the level
def right_side_view_dfs(root):
    if not root:
        return None
    rightest_at_depth = {}
    max_depth = -1
    stack = [(root, 0)]
    while stack:
        current, depth = stack.pop()
        max_depth = max(max_depth, depth)
        if depth not in rightest_at_depth:
            rightest_at_depth[depth] = current.val
        if current.left:
            stack.append((current.left, depth + 1))
        if current.right:
            stack.append((current.right, depth + 1))
    return [rightest_at_depth[depth] for depth in range(max_depth + 1)]

x = TreeNode.arr_to_binary_tree([1,2,3,None,5,None,4])
print(right_side_view_dfs(x))