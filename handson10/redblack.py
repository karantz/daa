class RBNode:
    def __init__(self, key, color="red"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = RBNode(key=None, color="black")
        self.root = self.NIL_LEAF

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.NIL_LEAF
        new_node.right = self.NIL_LEAF
        if self.root == self.NIL_LEAF:
            self.root = new_node
            self.root.color = "black"
            self.root.parent = None
        else:
            self._insert_recursive(self.root, new_node)
        self._fix_insert(new_node)

    def _insert_recursive(self, root, node):
        if node.key < root.key:
            if root.left == self.NIL_LEAF:
                root.left = node
                node.parent = root
            else:
                self._insert_recursive(root.left, node)
        else:
            if root.right == self.NIL_LEAF:
                root.right = node
                node.parent = root
            else:
                self._insert_recursive(root.right, node)

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_left(node.parent.parent)
        self.root.color = "black"

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def inorder(self):
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, result):
        if node != self.NIL_LEAF:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)
        return result

# Tests for Red-Black Tree
rbt = RedBlackTree()
