# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

from TreeNode import TreeNode
def zigzag(root):
    from collections import deque
    if not root:
        return []
    solution = []
    q = deque()
    q.append(root)
    level = 0
    while q:
        current_level = []
        if level % 2 == 0:
            for i in range(len(q)):
                current = q.popleft()
                current_level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        else:
            for i in range(len(q)):
                current = q.pop()
                current_level.append(current.val)
                if current.right:
                    q.appendleft(current.right)
                if current.left:
                    q.appendleft(current.left)
        solution.append(current_level)
        level += 1  
    return solution


t = TreeNode.arr_to_binary_tree([3,9,20,None,None,15,7])
print(zigzag(t))