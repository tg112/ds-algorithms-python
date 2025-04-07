## Array

### Time and Space Complexity of Array

| Operation                       | Time Complexity | Space Complexity |
|---------------------------------|-----------------|------------------|
| Creating an empty array         | O(1)            | O(1)             |
| Creating an array with elements | O(N)            | O(N)             |
| Inserting a value in an array   | O(N)            | O(1)             |
| Traversing a given array        | O(N)            | O(1)             |
| Accessing a given cell          | O(1)            | O(1)             |
| Searching a given value         | O(N)            | O(1)             |
| Deleting a given value          | O(N)            | O(1)             |

### Time and Space Complexity of Two Dimensional Array
| Operation                            | Time Complexity | Space Complexity |
|--------------------------------------|-----------------|------------------|
| Creating an empty array              | O(1)            | O(1)             |
| Creating an array with elements      | O(mn)           | O(mn)            |
| Inserting a column / row in an array | O(mn)           | O(mn)            |
| Traversing a given array             | O(mn)           | O(1)             |
| Accessing a given cell               | O(1)            | O(1)             |
| Searching a given value              | O(mn)           | O(1)             |
| Deleting a given value               | O(mn)           | O(mn)            |

### When to use/avoid array

**When to use**
- To store multiple variables of same data type
- Random access

**When to avoid**
- Same data type elements 
- Reserve memory

## Python Lists
- A list is a data structure that holds an ordered collection of items
- List can hold various data types. ex) `[1, 'a', 1.1, True, [2, 'b']]`


### Time and Space Complexity of Lists
| Operation                       | Time Complexity | Space Complexity |
|---------------------------------|-----------------|------------------|
| Creating an empty List          | O(1)            | O(1)             |
| Creating a list with elements   | O(n)            | O(n)             |
| Inserting a value in a list     | O(n)            | O(1)             |
| Traversing a list               | O(n)            | O(1)             |
| Accessing a given cell in List  | O(1)            | O(1)             |
| Searching a given value in List | O(n)            | O(1)             |
| Deleting a value from List      | O(1)            | O(1)             |

## Python dictionary
- A dictionary is a collection which is unordered, changeable and indexed

### Dictionary in memory
- A hash table is a way of doing key-value lookups. You store the values in an array, and then use a hash function to find the index of the array cell that corresponds to your key-value pair.

### Dictionary vs list
| Dictionary                                | List                                 |
|-------------------------------------------|--------------------------------------|
| Unordered                                 | Ordered                              |
| Access via keys                           | Access via index                     |
| Collection of key value pairs             | Collection of elements               |
| Preferred when you have unique key values | Preferred when you have ordered data |
| No duplicate members                      | Allow duplicate members              |

### Time and space complexity in python dictionary
| Operation                         | Time Complexity | Space Complexity |
|-----------------------------------|-----------------|------------------|
| Creating a Dictionary             | O(len(dict))    | O(n)             |
| Inserting a value in a dictionary | O(1)/O(n)       | O(1)             |
| Traversing a given dictionary     | O(n)            | O(1)             |
| Accessing a given cell            | O(1)            | O(1)             |
| Deleting a given value            | O(n)            | O(1)             |
| Searching a given value           | O(1)            | O(1)             |
