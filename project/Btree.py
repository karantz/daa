class BTreeNode:
    def __init__(self, t, is_leaf=True):
        self.t = t
        self.keys = []
        self.children = []
        self.is_leaf = is_leaf

    def __str__(self):
        return f"Keys: {self.keys}, Leaf: {self.is_leaf}"


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)
        self.t = t

    def search(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)

        if node.is_leaf:
            return None

        return self.search(key, node.children[i])

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(self.t, is_leaf=False)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(self.root, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1

        if node.is_leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        t = self.t
        child = parent.children[i]
        new_child = BTreeNode(t, is_leaf=child.is_leaf)
        mid = t - 1

        parent.keys.insert(i, child.keys[mid])
        parent.children.insert(i + 1, new_child)

        new_child.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]

        if not child.is_leaf:
            new_child.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]

    def delete(self, key, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            if node.is_leaf:
                node.keys.pop(i)
            else:
                self.delete_internal_node(node, key, i)
        elif not node.is_leaf:
            self.delete_from_child(node, key, i)
        else:
            print("Key not found in tree.")

    def delete_internal_node(self, node, key, i):
        if len(node.children[i].keys) >= self.t:
            predecessor = self.get_predecessor(node.children[i])
            node.keys[i] = predecessor
            self.delete(predecessor, node.children[i])
        elif len(node.children[i + 1].keys) >= self.t:
            successor = self.get_successor(node.children[i + 1])
            node.keys[i] = successor
            self.delete(successor, node.children[i + 1])
        else:
            self.merge(node, i)
            self.delete(key, node.children[i])

    def delete_from_child(self, node, key, i):
        child = node.children[i]
        if len(child.keys) < self.t:
            self.fill(node, i)
        self.delete(key, node.children[i])

    def get_predecessor(self, node):
        while not node.is_leaf:
            node = node.children[-1]
        return node.keys[-1]

    def get_successor(self, node):
        while not node.is_leaf:
            node = node.children[0]
        return node.keys[0]

    def merge(self, node, i):
        child = node.children[i]
        sibling = node.children[i + 1]
        mid = node.keys.pop(i)

        child.keys.append(mid)
        child.keys.extend(sibling.keys)
        if not sibling.is_leaf:
            child.children.extend(sibling.children)

        node.children.pop(i + 1)

    def fill(self, node, i):
        if i > 0 and len(node.children[i - 1].keys) >= self.t:
            self.borrow_from_prev(node, i)
        elif i < len(node.children) - 1 and len(node.children[i + 1].keys) >= self.t:
            self.borrow_from_next(node, i)
        else:
            if i > 0:
                self.merge(node, i - 1)
            else:
                self.merge(node, i)

    def borrow_from_prev(self, node, idx):
        """
        Borrow a key from the previous sibling of the child at index idx.
        """
        child = node.children[idx]
        sibling = node.children[idx - 1]

        # Shift all keys and children in child to make space for a new key
        child.keys.insert(0, node.keys[idx - 1])
        if not child.is_leaf:
            child.children.insert(0, sibling.children.pop(-1))

        # Move the last key of the sibling to the parent
        node.keys[idx - 1] = sibling.keys.pop(-1)

    def borrow_from_next(self, node, idx):
        """
        Borrow a key from the next sibling of the child at index idx.
        """
        child = node.children[idx]
        sibling = node.children[idx + 1]

        # Move the first key of the sibling to the parent
        node.keys[idx] = sibling.keys.pop(0)

        # Move the first child of the sibling to the child node
        if not sibling.is_leaf:
            child.children.append(sibling.children.pop(0))

        # Add the borrowed key from the parent to the child
        child.keys.append(node.keys[idx])

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, "Keys:", node.keys)
        for child in node.children:
            self.display(child, level + 1)

if __name__ == "__main__":
    t = int(input("Enter the minimum degree of the B-Tree (t): "))
    btree = BTree(t)

    while True:
        print("\nOptions:")
        print("1. Insert a key")
        print("2. Search for a key")
        print("3. Delete a key")
        print("4. Display the tree")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter the key to insert: "))
            btree.insert(key)
            print(f"Inserted {key} into the B-Tree.")
        elif choice == "2":
            key = int(input("Enter the key to search: "))
            result = btree.search(key)
            if result:
                node, index = result
                print(f"Found key {node.keys[index]} in node with keys {node.keys}")
            else:
                print("Key not found.")
        elif choice == "3":
            key = int(input("Enter the key to delete: "))
            btree.delete(key)
            print(f"Deleted {key} from the B-Tree.")
        elif choice == "4":
            print("B-Tree structure:")
            btree.display()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
