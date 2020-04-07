# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
#  
# 
# Example 1:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
#  
# 
# Note:
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.

from TreeNode import TreeNode


# This method stores all the ancestors of all the nodes in a dictionary and finds the common ancestor with the highest level
# Works in O(n) time since we have to find the ancestors for every node, but O(n log n) space (I think..) since every node has to store all the ancestors.  n keys in the dictionary, and values, which are ancestors, will be proportional to the height of the tree
def lca_slow(root, p, q):
    from collections import defaultdict
    d = defaultdict(list)
    s = [(root, 0)]
    while s:
        current, level = s.pop()
        if current == p:
            p_l = (current, level)
        if current == q:
            q_l = (current, level)
        d[(current, level)].append((current, level))
        if current.left:
            s.append((current.left, level+1))
            d[(current.left, level+1)].extend(d[(current, level)])
        if current.right:
            s.append((current.right, level+1))
            d[(current.right, level+1)].extend(d[(current, level)])
    if p_l in d[q_l]:
        return p
    if q_l in d[p_l]:
        return q
    d[p_l].remove(p_l)
    d[q_l].remove(q_l)
    common_ancestors = [x for x in d[p_l]+d[q_l] if (x in d[p_l] and x in d[q_l])]
    max_level = 0
    sol = root
    for node, level in common_ancestors:
        if level > max_level:
            sol = node
    return sol

# Recursive solution.  We use three flags, left, right and current to check whether left/right subtree contains p,q.
# We use current since the node itself is considered its descendent.  If any two flags are True, that node is the
# lowest common ancestor.  O(n) time since worst case is visiting all nodes, and O(N) space from stack space 
def lca_rec(root, p, q):
    ans = []
    def recurse(node, ans):
        if not node:
            return False
        left = recurse(node.left, ans)
        right = recurse(node.right, ans)
        current = (node == p or node == q)
        if left + right + current >= 2:
            ans.append(node)
        return left or right or current
    recurse(root, ans)
    return ans[0]


# Iterative approach using dfs.  We add a parent field to each node until we find both p and q.
# Then we create a set for all of p's ancestors, and go up q's ancestors till we meet a match
# O(n) time since worse case we go through all the nodes and O(n) space for same reason
def lca_iter(root, p, q):
    root.parent = None
    found_p, found_q = False, False
    s = [root]
    while s:
        current = s.pop()
        if current == p:
            found_p = True
        if current == q:
            found_q = True
        if found_p and found_q:
            break
        if current.left:
            current.left.parent = current
            s.append(current.left)
        if current.right:
            current.right.parent = current
            s.append(current.left)
    ancestors = {}
    while p:
        ancestors.add(p)
        p = p.parent
    while q not in ancestors:
        q = q.parent
    return q

# x = TreeNode.arr_to_binary_tree([3,5,1,6,2,0,8,None,None,7,4])
x = TreeNode.arr_to_binary_tree([-1,0,3,-2,4,None,None,8])
print(lca_rec(x, x.right, x.left.left.left))
