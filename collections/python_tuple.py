new_tuple = ('a', 'b', 'c', 'd')
print(new_tuple)
tuple1 = tuple('abecde')
print(tuple1) # ('a', 'b', 'e', 'c', 'd', 'e')

print('Tuples in memory / accessing an element of Tuple')
print(new_tuple[0])  # a
print(new_tuple[:3]) # ('a', 'b', 'c')
print(new_tuple[:])  # ('a', 'b', 'c', 'd')

# traverse a tuple
print('traverse a tuple')
for i in new_tuple: # O(n)
    print(i)

for i in range(len(new_tuple)): # O(n)
    print(new_tuple[i])

# Search for an element in Tuple
print('Search for an element in Tuple')
print('a' in new_tuple)     # True
print(new_tuple.index('b')) # 1

def search_tuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"The element is found at position {i}"
    return "The element is not found"

print(search_tuple(new_tuple, 'k'))

# Tuple operations / functions
tuple_one = (1,3,5,7)
tuple_two = (2,4,6,8)
print(tuple_one + tuple_two) # (1, 3, 5, 7, 2, 4, 6, 8)
print(tuple_one * 2)         # (1, 3, 5, 7, 1, 3, 5, 7)

print(tuple_one.count(1))    # 1
print(tuple_one.index(5))    # 2
print(len(tuple_one))        # 4
print(min(tuple_one))        # 1
print(max(tuple_one))        # 7
