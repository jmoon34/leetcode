# Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
# Example 1:
# Input:
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
# Note:
# The range of node's value is in the range of 32-bit signed integer.

from TreeNode import TreeNode

def avg_of_levels_iter(root):
    if not root:
        return []
    solution = []
    q = [root]
    while q:
        next_level = []
        avg = 0
        for node in q:
            avg += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        avg /= len(q)
        solution.append(avg)
        q = next_level
    return solution

def avg_of_levels_recursion(root):
    solution = []
    def recurse(node, level):
        if not node:
            return []
        if len(solution) < level:
            solution.append([])
        solution[level-1].append(node.val)
        if node.left:
            recurse(node.left, level+1)
        if node.right:
            recurse(node.right, level+1)
    recurse(root, 1)
    return [sum(x)/len(x) for x in solution]

x = TreeNode.arr_to_binary_tree([3,9,20,None,None,15,7])
print(avg_of_levels_recursion(x))