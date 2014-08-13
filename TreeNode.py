class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def inorder_print(self):
        print self.val,
        if self.left:
            self.left.inorder_print(),
        if self.right:
            self.right.inorder_print(),

    def preorder_print(self):
        if self.left:
            self.left.preorder_print()
        print self.val,
        if self.right:
            self.right.preorder_print()

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)
