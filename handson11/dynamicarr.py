class DynamicArray:
    def __init__(self):
        self._capacity = 1
        self._size = 0
        self._data = self._make_array(self._capacity)

    def _make_array(self, capacity):
        return [None] * capacity

    def _resize(self, new_capacity):
        new_data = self._make_array(new_capacity)
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def push_back(self, value):
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._data[self._size] = value
        self._size += 1

    def pop_back(self):
        if self._size == 0:
            raise IndexError("pop from empty array")
        self._data[self._size - 1] = None
        self._size -= 1

    def get_size(self):
        return self._size

    def get_capacity(self):
        return self._capacity

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("index out of bounds")
        return self._data[index]

# Text-based interface
def text_based_ui():
    arr = DynamicArray()
    while True:
        print("\nDynamic Array Interface")
        print("1. Add element (push_back)")
        print("2. Remove last element (pop_back)")
        print("3. View array elements")
        print("4. Get size")
        print("5. Get capacity")
        print("6. Exit")
        
        choice = input("Select an option: ")

        if choice == '1':
            value = int(input("Enter value to add: "))
            arr.push_back(value)
            print(f"{value} added.")

        elif choice == '2':
            try:
                arr.pop_back()
                print("Last element removed.")
            except IndexError as e:
                print(e)

        elif choice == '3':
            print("Array elements:", [arr[i] for i in range(arr.get_size())])

        elif choice == '4':
            print("Size:", arr.get_size())

        elif choice == '5':
            print("Capacity:", arr.get_capacity())

        elif choice == '6':
            print("Exiting.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    text_based_ui()
