from binary import BinarySearchTree
from avltree import AVLTree 
from redblack import RedBlackTree
def bst_menu():
    bst = BinarySearchTree()
    while True:
        print("\nBinary Search Tree Menu:")
        print("1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Display (In-order)")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter the number to insert: "))
            bst.insert(key)
            print(f"{key} inserted.")
        elif choice == '2':
            key = int(input("Enter the number to delete: "))
            bst.delete(key)
            print(f"{key} deleted.")
        elif choice == '3':
            key = int(input("Enter the number to search: "))
            found = bst.search(key)
            print(f"{key} found: {found}")
        elif choice == '4':
            print("In-order Traversal:", bst.inorder())
        elif choice == '5':
            break
        else:
            print("Invalid choice! Please try again.")

def rbt_menu():
    rbt = RedBlackTree()
    while True:
        print("\nRed-Black Tree Menu:")
        print("1. Insert")
        print("2. Display (In-order)")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter the number to insert: "))
            rbt.insert(key)
            print(f"{key} inserted.")
        elif choice == '2':
            print("In-order Traversal:", rbt.inorder())
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again.")

def avl_menu():
    avl = AVLTree()
    while True:
        print("\nAVL Tree Menu:")
        print("1. Insert")
        print("2. Delete")
        print("3. Display (In-order)")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            key = int(input("Enter the number to insert: "))
            avl.insert(key)
            print(f"{key} inserted.")
        elif choice == '2':
            key = int(input("Enter the number to delete: "))
            avl.delete(key)
            print(f"{key} deleted.")
        elif choice == '3':
            print("In-order Traversal:", avl.inorder())
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Binary Search Tree")
        print("2. Red-Black Tree")
        print("3. AVL Tree")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bst_menu()
        elif choice == '2':
            rbt_menu()
        elif choice == '3':
            avl_menu()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
