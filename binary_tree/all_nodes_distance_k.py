# We are given a binary tree (with root node root), a target node, and an integer value K.
#
# Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
#
#
#
# Example 1:
#
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#
#
#
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these objects.
#
#
# Note:
#
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.

from TreeNode import TreeNode

def k_away(root, target, K):
    from collections import deque
    def dfs(node, parent=None):
        if node:
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
    dfs(root)

    q = deque([(target, 0)])
    seen = {target}
    while q:
        if q[0][1] == K:
            return [node.val for node, d in q]
        current, distance = q.popleft()
        for neighbor in (current.left, current.right, current.parent):
            if neighbor and neighbor not in seen:
                seen.add(neighbor)
                q.append((neighbor, distance+1))
    return []

x = TreeNode.arr_to_binary_tree([3,5,1,6,2,0,8,None,None,7,4])

print(x.par)
TreeNode.in_order_traversal_rec(x)
#print(k_away(x, x.right.left, 2))