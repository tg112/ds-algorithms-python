# Accessing/Traversing the list
shopping_list = ['apple', 'banana', 'orange']

# Accessing
print(shopping_list[0])

# Is apple contained in a list
print('apple' in shopping_list) # True

# Traversing
for item in shopping_list:
    print(item)

for i in range(len(shopping_list)): # O(n)
    shopping_list[i] = shopping_list[i] + '+'
    print(shopping_list[i])

# Update/Insert a list
print('update/insert a list')
num_list = [1,2,3,4,5,6]

# update
num_list[2] = 'update' # O(1)
print(num_list) # 1, 2, 'update', 4, 5, 6]
# insert
num_list.insert(1, 'inserted') # O(n)
print(num_list) # [1, 'inserted', 2, 'update', 4, 5, 6]

num_list.append('appended') # O(1)
print(num_list) # [1, 'inserted', 2, 'update', 4, 5, 6, 'appended']

new_list = ['new', 'list']
num_list.extend(new_list) # O(n)
print(num_list) # [1, 'inserted', 2, 'update', 4, 5, 6, 'appended', 'new', 'list']

# Slice / Deletion a list
char_list = ['a', 'b', 'c', 'd', 'e', 'f']

# slice
print(char_list[0: 2]) # ['a', 'b']
print(char_list[1: 3]) # ['b', 'c']
print(char_list[: 4]) # ['a', 'b', 'c', 'd']
print(char_list[3:]) # ['d', 'e', 'f']

# delete / pop O(1)/O(n)
char_list.pop() # ['a', 'b', 'c', 'd', 'e']
print(char_list)
char_list.pop(1) # ['a', 'c', 'd', 'e']
print(char_list)

# delete / delete O(n)
del char_list[0] # ['c', 'd', 'e']
print(char_list)
del char_list[0:1] # ['d', 'e']
print(char_list)

# delete / remove O(n)
char_list.remove('e') # ['d']
print(char_list)

# Searching for an element in a List
print('Searching for an element in a List')
searching_list = [10,20,30,40,50,60,70,80,90]
target = 50
if target in searching_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

# Linear Search
def linear_search(p_list, p_target):
    # enumerateはindexを返す
    for i, value in enumerate(p_list): # O(n)
        if value == p_target:          # O(1)
            return i                   # O(1)
    return -1                          # O(1)

print(linear_search(searching_list, 30))

# List Operations / Functions
print('List Operations / Functions')
a = [1,2,3]
b = [4,5,6]

c = a + b
print('+ operator: ', c) # [1, 2, 3, 4, 5, 6]

d = [0, 1]
d = d * 4
print('* operator: ', d) # [0, 1, 0, 1, 0, 1, 0, 1]

e = [0,1,2,3,4,5,6]
print('len function:' , len(e)) # 7
print('max function: ', max(e)) # 6
print('min function: ', min(e)) # 0
print('sum function: ', sum(e)) # 21
print('average: ', sum(e) / len(e)) # 3.0

# List and strings
a = 'spam spam spam'
string_list = list(a)
split_string = a.split()
delimiter = a.split('-')
join_delimiter = ' '.join(delimiter)
print(string_list)    # ['s', 'p', 'a', 'm', ' ', 's', 'p', 'a', 'm', ' ', 's', 'p', 'a', 'm']
print(split_string)   # ['spam', 'spam', 'spam']
print(delimiter)      # ['spam spam spam']
print(join_delimiter) # spam spam spam

# List comprehension
print('List comprehension: [new_val for val in list')
temp_list = [1,2,3]
new_list = [val * 2 for val in temp_list]
print(new_list) # [2, 4, 6]

# Conditional list comprehension
print('Conditional list comprehension: [new_val for val in list if condition]')
prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
updated_list = [number for number in prev_list if number > 0]
print(updated_list) # [10, 2, 60, 45, 20]

sentence = 'hello world'
def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print(consonants) # ['h', 'l', 'l', 'w', 'r', 'l', 'd']