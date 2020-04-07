class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self)

    @staticmethod
    def in_order_traversal_rec(node):
        if not node:
            return
        TreeNode.in_order_traversal_rec(node.left)
        print(node.val, end=" ")
        TreeNode.in_order_traversal_rec(node.right)

    @staticmethod
    def in_order_traversal_iter(root):
        stack = [root]
        current = root
        while stack or current:
            while current:
                if current != root:
                    stack.append(current)
                current = current.left
            node = stack.pop()
            print(node.val, end=" ")
            current = node.right

    @staticmethod
    def pre_order_traversal_rec(node):
        if not node:
            return
        print(node.val, end=" ")
        TreeNode.pre_order_traversal_rec(node.left)
        TreeNode.pre_order_traversal_rec(node.right)

    @staticmethod
    def pre_order_traversal_iter(root):
        stack = [root]
        while stack:
            current = stack.pop()
            print(current.val, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)


    @staticmethod
    def arr_to_binary_tree(arr):
        def build(i):
            if i >= len(arr) or arr[i] is None:
                return None
            node = TreeNode(arr[i])
            node.left = build(2*i+1)
            node.right = build(2*i+2)
            return node
        return build(0)


x = TreeNode.arr_to_binary_tree([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# TreeNode.in_order_traversal_rec(x)
# print()
# TreeNode.in_order_traversal_iter(x)
