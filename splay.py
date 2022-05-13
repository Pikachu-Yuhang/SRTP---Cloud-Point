class Node:
    n = 1
    rasterize = False
    def __init__(self, key):
        self.key = key
        self.left = self.right = None

class SplayTree:
    def __init__(self):
        self.root = None
        self.header = Node(None) #For splay()

    def insert(self, key):
        if (self.root == None):
            self.root = Node(key)
            return

        self.splay(key)
        if self.root.key == key:
            # If the point is already there in the tree, add one to n.
            self.root.n = self.root.n + 1
            return

        n = Node(key)
        if key < self.root.key:
            n.left = self.root.left
            n.right = self.root
            self.root.left = None
        else:
            n.right = self.root.right
            n.left = self.root
            self.root.right = None
        self.root = n

    def remove(self, key):
        self.splay(key)
        if key != self.root.key:
            raise 'key not found in tree'

        # Now delete the root.
        if self.root.left== None:
            self.root = self.root.right
        else:
            x = self.root.right
            self.root = self.root.left
            self.splay(key)
            self.root.right = x

    def findMin(self):
        if self.root == None:
            return None
        x = self.root
        while x.left != None:
            x = x.left
        self.splay(x.key)
        return x.key

    def findMax(self):
        if self.root == None:
            return None
        x = self.root
        while (x.right != None):
            x = x.right
        self.splay(x.key)
        return x.key

    def find(self, key):
        if self.root == None:
            return None
        self.splay(key)
        if self.root.key != key:
            return None
        return self.root.key

    def isEmpty(self):
        return self.root == None
    
    def splay(self, key):
        l = r = self.header
        t = self.root
        self.header.left = self.header.right = None
        while True:
            if key < t.key:
                if t.left == None:
                    break
                if key < t.left.key:
                    y = t.left
                    t.left = y.right
                    y.right = t
                    t = y
                    if t.left == None:
                        break
                r.left = t
                r = t
                t = t.left
            elif key > t.key:
                if t.right == None:
                    break
                if key > t.right.key:
                    y = t.right
                    t.right = y.left
                    y.left = t
                    t = y
                    if t.right == None:
                        break
                l.right = t
                l = t
                t = t.right
            else:
                break
        l.right = t.left
        r.left = t.right
        t.left = self.header.right
        t.right = self.header.left
        self.root = t
    
    def preorder(self, node: Node):
        if (node == None):
            return
        print(node.key)
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node: Node):
        if (node == None):
            return
        self.inorder(node.left)
        print(node.key)
        print(node.n)
        self.inorder(node.right)
    
    def postorder(self, node: Node):
        if (node == None):
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.key)
    
    def traverse(self, node: Node, threshold: int, rasterized_point_set: list):
        if (node == None):
            return
        self.traverse(node.left, threshold, rasterized_point_set)
        if (node.n > threshold):
            node.rasterize = True
            rasterized_point_set.append(node.key)
        self.traverse(node.right, threshold, rasterized_point_set)
