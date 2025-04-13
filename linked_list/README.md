# LinkedList

- Linked List is a form of a sequential collection and it does not have to be in order. A Linked list is made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link.
- Memory上では、それぞれのnodeがランダムに割り当てられる

TODO: add image here

## Types of Linked Lists

- singly Linked List
- Circular Linked List
- Doubly Linked List
- Circular Doubly Linked List

TODO: add image here

### Node Class

**(Node)** 10 ->

```python
# Node Class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
```

**Insertion to Linked List in Memory**
1. At the beginning of the linked list.
2. After a node in the middle of linked list 
3. At the end of the linked list.

### Time and Space Complexity of Singly Linked List
|                  | time complexity | space complexity |
|------------------|-----------------|------------------|
| Create           | O(1)            | O(1)             |
| Append           | O(1)            | O(1)             |
| Prepend          | O(1)            | O(1)             |
| Insert           | O(n)            | O(1)             |
| Search           | O(n)            | O(1)             |
| Traverse         | O(n)            | O(1)             |
| Get              | O(n)            | O(1)             |
| Set              | O(n)            | O(1)             |
| Pop first        | O(1)            | O(1)             |
| Pop              | O(n)            | O(1)             |
| Remove           | O(n)            | O(1)             |      
| Delete all nodes | O(1)            | O(1)             | 