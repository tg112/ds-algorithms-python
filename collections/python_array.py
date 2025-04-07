from array import *

# 1. Create an array and Traverse
# 第一引数は型、第二引数は初期値
my_array = array('i', [1,2,3,4])

for i in my_array: # O(n)
    print(i)

# 2. Access individual elements through indexes
print('Access individual elements through indexes')
print(my_array[0]) # O(1)

# 3. Append any value to the array using append() method
print('Append any value to the array using append() method')
my_array.append(5)
print(my_array)

# 4. Insert value in an array using insert() method
print('Insert value in an array using insert() method')
my_array.insert(0, 11)
print(my_array)

# 5. extend python array using extend() method
print('extend python array using extend() method')
my_array1 = array('i',[10,11,12,13])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print('Add items from list into array using fromlist() method')
temp_list = [20, 21, 22]
my_array.fromlist(temp_list)
print(my_array)

# 7. Remove any array element using remove() method
print('Remove any array element using remove() method')
my_array.remove(12)
print(my_array)

# 8. Remove any array element using pop() method
print('Remove any array element using pop() method')
my_array.pop()
print(my_array)

# 9. Fetch any element through its index using index() method
print('Fetch any element through its index using index() method')
print(my_array.index(13))

# 10. Reverse a python array using reverse() method
print('Reverse a python array using reverse() method')
my_array.reverse()
print(my_array)

# 11. Get array buffer information through buffer_info() method
print('Get array buffer information through buffer_info() method')
print(my_array.buffer_info())

# 12. Check for number of occurrences of an element using count() method
print('Check for number of occurrences of an element using count() method')
print(my_array.count(11))

# 13. Slice elements from an array
print('Slice elements from an array')
# [何番目: index]
print(my_array[2:4])

# 14. Convert array to a python list with same elements using tolist() method
print('Convert array to a python list with same elements using tolist() method')
print(my_array.tolist())

print("Two dimensional array below from here")

# Two Dimensional Array
import numpy as np

two_dimension = np.array([[1,2,3],[4,5,6]])
print(two_dimension)

# Insertion - Two Dimensional Array
# Adding Column / Time complexity O(mn)
# Adding Row / Time complexity O(mn)

new_two_dimension = np.append(two_dimension,  [[7,8,9]], axis=0)
print(new_two_dimension)

new_two_dimension = np.insert(two_dimension,  1, [[7,8,9]], axis=0)
print(new_two_dimension)

# Accessing two-dimensional array
print('Accessing two-dimensional array')
def access_elements(array, rowIndex,columnIndex):
    if rowIndex >= len(array):
        print('Incorrect row index')
    else:
        print(array[rowIndex][columnIndex])

access_elements(new_two_dimension, 1, 2) # O(1)

# Traversing two-dimensional array
print('Traversing two-dimensional array')
def traverse_elements(two_dimensional):
    for row in range(len(two_dimensional)): # O(mn)
        for column in range(len(two_dimensional[0])): # O(n)
            print(two_dimensional[row][column]) # O(1)

traverse_elements(new_two_dimension)

# Searching two-dimensional array
print('Searching two-dimensional array')
def search_elements(two_dimensional_array, value):
    for row in range(len(two_dimensional_array)):           # O(mn)
        for column in range(len(two_dimensional_array[0])): # O(n)
            if two_dimensional_array[row][column] == value: # O(1)
                return 'The element is located at row {}, column {}'.format(row, column)

    return 'The element is not found'
print(search_elements(new_two_dimension, 11))

# Deletion two-dimensional array
print('Deletion two-dimensional array')
# delete column
new_td_array = np.delete(new_two_dimension, 1, axis=0)
print(new_td_array)
# delete row
new_td_array = np.delete(new_two_dimension, 2, axis=1)
print(new_td_array)

