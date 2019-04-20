class Node:

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def __hash__(self):
        return hash(self.data)

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Postorder traversal
# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.right)
            res = res + self.PostorderTraversal(root.left)
            res.append(root.data)
        return res
'''
right1 = Node("A", None, None)
left = Node("NP", None, None)
right = Node("VP", None, right1)
root = Node("S", left, right)
print(root.PostorderTraversal(root))'''