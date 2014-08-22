import random


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    @staticmethod
    def create_from_array(array):
        return TreeNode.create_from_array_rec(array, 0, len(array)-1)

    @staticmethod
    def create_from_array_rec(array, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        node = TreeNode(array[mid])
        node.left = TreeNode.create_from_array_rec(array, start, mid-1)
        node.right = TreeNode.create_from_array_rec(array, mid+1, end)
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node
        return node

    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print self.val,
        if self.right:
            self.right.inorder_print()

    def preorder_print(self):
        print self.val,
        if self.left:
            self.left.preorder_print(),
        if self.right:
            self.right.preorder_print(),

    def postorder_print(self):
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print self.val,

    def inorder_print_advanced(self):
        cur = self
        while cur:
            if not cur.left:
                print cur.val,
                cur = cur.right
            else:
                # find predecessor
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    tmp.right = None
                    print cur.val,
                    cur = cur.right

    def preorder_print_advanced(self):
        cur = self
        while cur:
            if not cur.left:
                print cur.val,
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    print cur.val,
                    cur = cur.left
                else:
                    tmp.right = None
                    cur = cur.right

    def postorder_print_advanced(self):
        dummy = TreeNode()
        dummy.left = self
        cur = dummy
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    # reversely print from cur.left to tmp
                    cur.left.reverse_print(tmp)
                    tmp.right = None
                    cur = cur.right

    def reverse_print(self, to):
        cur = self
        res = []
        while cur != to:
            res.append(cur)
            cur = cur.right
        res.append(to)
        while res:
            print res.pop().val,

    def clone(self):
        root = TreeNode(self.val)
        if self.left:
            root.left = self.left.clone()
        if self.right:
            root.right = self.right.clone()
        return root

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

if __name__ == '__main__':
    array = [random.randint(0, 10000) for i in xrange(20)]
    # array = [1, 1, 42]
    print array
    root1 = TreeNode.create_from_array(array)
    root1.inorder_print()
    print '-----',
    root1.preorder_print()
    print
    root2 = root1.clone()
    root2.inorder_print()
    print '-----',
    root2.preorder_print()
    print
    root2.inorder_print_advanced()
    print '-----',
    root2.preorder_print_advanced()
    print
    root2.postorder_print()
    print
    root2.postorder_print_advanced()
