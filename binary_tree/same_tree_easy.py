# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false


def same_tree_rec(p, q):
    def recurse(n1, n2):
        if (not n1 and n2) or (n1 and not n2):
            return False
        if (not n1 and not n2):
            return True
        if n1.val != n2.val:
            return False
        return recurse(n1.left, n2.left) and recurse(n1.right, n2.right)
    return recurse(p, q)

# Use dfs to go through the tree and see if we get the same result
def same_tree_iter(p, q):
    if not p and not q:
        return True
    if (not p and q) or (p and not q):
        return False
    s1, s2 = [p], [q]
    while s1 and s2:
        c1 = s1.pop()
        c2 = s2.pop()
        if c1.val != c2.val:
            return False
        if (c1.left and not c2.left) or (not c1.left and c2.left) or (c1.right and not c2.right) or (
                not c1.right and c2.right):
            return False
        if c1.left:
            s1.append(c1.left)
        if c1.right:
            s1.append(c1.right)
        if c2.left:
            s2.append(c2.left)
        if c2.right:
            s2.append(c2.right)
    return True
