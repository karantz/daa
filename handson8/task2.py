class FixedSizeStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [0] * capacity
        self.top = -1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top += 1
        self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.stack[self.top]
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return self.top + 1


class FixedSizeQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [0] * capacity
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return value

    def front_value(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def size(self):
        return self.count


class FixedSizeSinglyLinkedList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [0] * capacity
        self.next = [-1] * capacity
        self.head = -1
        self.free = 0
        self.size_of_list = 0

        for i in range(capacity - 1):
            self.next[i] = i + 1
        self.next[capacity - 1] = -1

    def insert_at_beginning(self, value):
        if self.size_of_list == self.capacity:
            raise OverflowError("Linked List is full")
        new_node = self.free
        self.free = self.next[new_node]
        self.data[new_node] = value
        self.next[new_node] = self.head
        self.head = new_node
        self.size_of_list += 1

    def insert_at_end(self, value):
        if self.size_of_list == self.capacity:
            raise OverflowError("Linked List is full")
        new_node = self.free
        self.free = self.next[new_node]
        self.data[new_node] = value
        self.next[new_node] = -1
        if self.head == -1:
            self.head = new_node
        else:
            current = self.head
            while self.next[current] != -1:
                current = self.next[current]
            self.next[current] = new_node
        self.size_of_list += 1

    def delete(self, value):
        if self.is_empty():
            raise IndexError("Linked List is empty")
        current = self.head
        prev = -1
        while current != -1:
            if self.data[current] == value:
                if prev == -1:
                    self.head = self.next[current]
                else:
                    self.next[prev] = self.next[current]
                self.next[current] = self.free
                self.free = current
                self.size_of_list -= 1
                return True
            prev = current
            current = self.next[current]
        return False

    def search(self, value):
        current = self.head
        while current != -1:
            if self.data[current] == value:
                return True
            current = self.next[current]
        return False

    def is_empty(self):
        return self.size_of_list == 0

    def size(self):
        return self.size_of_list


# Menu-driven program to simulate switch-case
def menu():
    print("\nSelect Data Structure:")
    print("1. Stack")
    print("2. Queue")
    print("3. Singly Linked List")
    print("4. Exit")
    return int(input("Enter choice: "))

def stack_operations():
    stack = FixedSizeStack(5)
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Size")
        print("7. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            value = int(input("Enter value to push: "))
            stack.push(value)
            print("Value pushed.")
        elif choice == 2:
            print("Popped value:", stack.pop())
        elif choice == 3:
            print("Peek value:", stack.peek())
        elif choice == 4:
            print("Is stack empty:", stack.is_empty())
        elif choice == 5:
            print("Is stack full:", stack.is_full())
        elif choice == 6:
            print("Stack size:", stack.size())
        elif choice == 7:
            break

def queue_operations():
    queue = FixedSizeQueue(5)
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front Value")
        print("4. Check if Empty")
        print("5. Check if Full")
        print("6. Size")
        print("7. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            value = int(input("Enter value to enqueue: "))
            queue.enqueue(value)
            print("Value enqueued.")
        elif choice == 2:
            print("Dequeued value:", queue.dequeue())
        elif choice == 3:
            print("Front value:", queue.front_value())
        elif choice == 4:
            print("Is queue empty:", queue.is_empty())
        elif choice == 5:
            print("Is queue full:", queue.is_full())
        elif choice == 6:
            print("Queue size:", queue.size())
        elif choice == 7:
            break

def linked_list_operations():
    linked_list = FixedSizeSinglyLinkedList(5)
    while True:
        print("\nLinked List Operations:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Delete")
        print("4. Search")
        print("5. Check if Empty")
        print("6. Size")
        print("7. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            value = int(input("Enter value to insert: "))
            linked_list.insert_at_beginning(value)
            print("Value inserted at beginning.")
        elif choice == 2:
            value = int(input("Enter value to insert: "))
            linked_list.insert_at_end(value)
            print("Value inserted at end.")
        elif choice == 3:
            value = int(input("Enter value to delete: "))
            if linked_list.delete(value):
                print("Value deleted.")
            else:
                print("Value not found.")
        elif choice == 4:
            value = int(input("Enter value to search: "))
            print("Value found:", linked_list.search(value))
        elif choice == 5:
            print("Is linked list empty:", linked_list.is_empty())
        elif choice == 6:
            print("Linked list size:", linked_list.size())
        elif choice == 7:
            break

if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == 1:
            stack_operations()
        elif choice == 2:
            queue_operations()
        elif choice == 3:
            linked_list_operations()
        elif choice == 4:
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
