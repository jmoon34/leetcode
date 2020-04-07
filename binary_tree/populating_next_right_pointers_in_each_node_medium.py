# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#
#
# Follow up:
#
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#
#
# Example 1:
#
#
#
# Input: root = [1,2,3,4,5,6,7]
# Output: [1,#,2,3,#,4,5,6,7,#]
# Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
#
#
# Constraints:
#
# The number of nodes in the given tree is less than 4096.
# -1000 <= node.val <= 1000

# recursive solution O(n) time since we have to go through every node and O(n) space since we use up stack space for
# the recursion
def connect(self, root):
    if not root:
        return None
    if not root.left:
        return root
    def recurse(node, right):
        node.next = right
        if not node.left:  # termination condition: node is leaf
            return
        recurse(node.left, node.right)
        if node.next:
            recurse(node.right, node.next.left)
        else:
            recurse(node.right, None)
    recurse(root.left, root.right)
    recurse(root.right, None)
    return root

# recursive solution O(n) time and O(1) space.  Resembles traveling through a linked-list, always starting from
# the left most node and setting the pointers for the level underneath it while traversing
def connect_2(self, root):
    if not root:
        return None
    leftest = root
    while leftest.left:
        current = leftest
        print(current.val)
        while current.next:
            current.left.next = current.right
            current.right.next = current.next.left
            current = current.next
        current.left.next = current.right
        leftest = leftest.left
    return root


def connect_iter(self, root):
    if not root:
        return None
    from collections import deque
    q = deque()
    q.append(root)
    while q:
        n = len(q)
        for i in range(n):
            current = q.popleft()
            if i != n - 1:
                current.next = q[0]
            if current.left:
                q.append(current.left)
                q.append(current.right)
    return root