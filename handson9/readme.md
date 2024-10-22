Key Components:
Doubly Linked List: This handles collisions via chaining.

insert: Adds a new node to the end of the list.
remove: Removes the node with the given key, updating next and prev pointers.
search: Returns the node with the specified key if found.
clear: Clears the list.
Hash Function: Implements the multiplication method for hash calculation:

ℎ(𝑘)=⌊𝑚⋅(𝑘⋅𝐴 mod 1)⌋
Where 

m is the table size, 

A is the multiplication constant.

Dynamic Resizing:

If the load factor exceeds 0.75, the table size is doubled.
If the load factor drops below 0.25, the table size is halved.
On resizing, all items are re-hashed into the new table.


How the Hash Table Works:

Insertions: The key is hashed, and the value is inserted into the appropriate doubly linked list. The table resizes if necessary.
Search: The key is hashed, and the value is searched in the appropriate list.
Removals: The key is hashed, and the corresponding node is removed from the list.
Resizing: The table doubles or halves in size depending on the load factor, and all entries are re-hashed.

/h output :
![image](https://github.com/user-attachments/assets/71c77a72-7c03-43bf-8fc0-34f720b90615)


![image](https://github.com/user-attachments/assets/e83f3f6e-7df0-413e-a34d-661d8fee1ca9)



