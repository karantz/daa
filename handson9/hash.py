import math

# Node for Doubly Linked List
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

# Doubly Linked List for Chaining
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, key, value):
        new_node = Node(key, value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # remove head

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev  # remove tail

                return True  # Key was found and removed
            current = current.next
        return False  # Key not found

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def clear(self):
        self.head = self.tail = None

    def display(self):
        current = self.head
        while current:
            print(f"({current.key}, {current.value})", end=" <-> ")
            current = current.next
        print("None")

# Hash Table using Multiplication Hashing Method and Chaining
class HashTable:
    def __init__(self, initial_size=8):
        self.table_size = initial_size
        self.item_count = 0
        self.table = [DoublyLinkedList() for _ in range(self.table_size)]
        self.load_factor_max = 0.75
        self.load_factor_min = 0.25

    # Hash function (multiplication method)
    def hash_function(self, key):
        A = (math.sqrt(5) - 1) / 2  # constant A for multiplication method
        return int(self.table_size * ((key * A) % 1))

    # Resize table when needed
    def resize_table(self, new_size):
        old_table = self.table
        self.table = [DoublyLinkedList() for _ in range(new_size)]
        old_table_size = self.table_size
        self.table_size = new_size

        for i in range(old_table_size):
            current = old_table[i].head
            while current:
                new_hash = self.hash_function(current.key)
                self.table[new_hash].insert(current.key, current.value)
                current = current.next

    # Ensure that resizing is handled on insertions/deletions
    def check_resize(self):
        load_factor = self.item_count / self.table_size
        if load_factor > self.load_factor_max:
            self.resize_table(self.table_size * 2)
        elif load_factor < self.load_factor_min and self.table_size > 1:
            self.resize_table(self.table_size // 2)

    # Insert key-value pair
    def insert(self, key, value):
        hash_value = self.hash_function(key)
        self.table[hash_value].insert(key, value)
        self.item_count += 1
        self.check_resize()

    # Remove key
    def remove(self, key):
        hash_value = self.hash_function(key)
        if self.table[hash_value].remove(key):
            self.item_count -= 1
            self.check_resize()
            return True
        return False

    # Search for a value by key
    def search(self, key):
        hash_value = self.hash_function(key)
        node = self.table[hash_value].search(key)
        return node.value if node else None

    # Display the hash table contents
    def display(self):
        print("\nHash Table contents:")
        for i in range(self.table_size):
            print(f"Bucket {i}:", end=" ")
            self.table[i].display()

# Menu-based system for the Hash Table
def menu():
    ht = HashTable()

    while True:
        print("\nOptions:")
        print("1. Insert key-value pair")
        print("2. Search by key")
        print("3. Remove by key")
        print("4. Display hash table")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            key = int(input("Enter key (integer): "))
            value = int(input("Enter value (integer): "))
            ht.insert(key, value)
            print(f"Inserted ({key}, {value}) into the hash table.")

        elif choice == '2':
            key = int(input("Enter key to search (integer): "))
            result = ht.search(key)
            if result is not None:
                print(f"Found: ({key}, {result})")
            else:
                print("Key not found.")

        elif choice == '3':
            key = int(input("Enter key to remove (integer): "))
            if ht.remove(key):
                print(f"Key {key} removed.")
            else:
                print("Key not found.")

        elif choice == '4':
            ht.display()

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
