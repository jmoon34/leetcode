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
    def in_order_traversal(node):
        if not node:
            return
        TreeNode.in_order_traversal(node.left)
        print(node.val, end=" ")
        TreeNode.in_order_traversal(node.right)

    @staticmethod
    def arr_to_binary_tree(arr):
        def build(i):
            if i >= len(arr) or not arr[i]:
                return None
            node = TreeNode(arr[i])
            node.left = build(2*i+1)
            node.right = build(2*i+2)
            return node
        return build(0)

x = TreeNode.arr_to_binary_tree([1,2,3,None,4,None,6])
#TreeNode.in_order_traversal(x)
