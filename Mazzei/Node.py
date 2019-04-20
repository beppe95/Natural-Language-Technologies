class Node:

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __hash__(self):
        return hash(self.data)

# Print the Tree
    def print_tree(self):
        print(self.data)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def get_list_tree(self, res):
        res.append(self)
        if self.left:
            self.left.get_list_tree(res)
        if self.right:
            self.right.get_list_tree(res)
        return res

# Post-order traversal
# Left ->Right -> Root
    def post_order_traversal(self, root):
        res = []
        if root:
            res = self.post_order_traversal(root.right)
            res = res + self.post_order_traversal(root.left)
            res.append(root.data)
        return res
