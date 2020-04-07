# Given preorder and inorder traversal of a tree, construct the binary tree.
# 
# Note:
# You may assume that duplicates do not exist in the tree.
# 
# For example, given
# 
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
# 
#     3
#    / \
#   9  20
#     /  \
#    15   7

from TreeNode import TreeNode

class solution:
    pre_index = 1
    def contruct_rec(self, preorder, inorder):
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        def recurse(node, left, right, split):
            l = inorder[left:split]
            r = inorder[split + 1:right]
            if l and r:
                print(l, r, self.pre_index)
            if l:
                node.left = TreeNode(preorder[self.pre_index])
                node_index = inorder.index(preorder[self.pre_index])
                self.pre_index += 1
                recurse(node.left, left, split, node_index)
            if r:
                node.right = TreeNode(preorder[self.pre_index])
                node_index = inorder.index(preorder[self.pre_index])
                self.pre_index += 1
                recurse(node.right, split + 1, right, node_index)

        recurse(root, 0, len(inorder), root_index)
        return root

# O(n) time since we have to iterate through every node, O(n) space since we have to create every node and store them in a stack
def construct_iter(preorder, inorder):
    io_index = {}
    for i in range(len(inorder)):
        io_index[inorder[i]] = i

    stack = []
    root = None

    for val in preorder:
        if not root:
            root = TreeNode(val)
            stack.append(root)
        else:
            node = TreeNode(val)
            if io_index[val] < io_index[stack[-1]]:
               stack[-1].left = node
            else:
                while stack and io_index[val] > io_index[stack[-1]]:
                    u = stack.pop()
                u.right = node
            stack.append(node)
    return root







p = [1,2,4,8,9,5,10,11,3,6,12,13,7,14,15]
i = [8,4,9,2,10,5,11,1,12,6,13,3,14,7,15]
s = solution()
x = construct_iter(p, i)
TreeNode.pre_order_traversal_iter(x)
print()
TreeNode.in_order_traversal_iter(x)
