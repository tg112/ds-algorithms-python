# Creating dictionary
import random

print('Creating dictionary')
dict_from_constructor = dict() # O(1)
print(dict_from_constructor)   # {}
my_dict = {}   # O(1)
print(my_dict) # {}

eng_jp = dict(hello='こんにちは', good_morning="おはよう") # O(n)
print(eng_jp)
eng_num = {'one': 1,'two': 2, 'three': 3} # O(n)
print(eng_num)

# Update / add an element to the dictionary
print('Update / add an element to the dictionary')
edy = {'name': 'Edy', 'age': 26}
print(edy)
edy['age'] = 30 # O(1)
print(edy['age'])
edy['address'] = 'NY' # O(1)
print(edy)

# Traversing through a dictionary

def traverse_dict(dict):
    # Keyのみ
    for key in dict: # O(n)
        print(key)   # O(1)
    # Valueのみ
    for val in dict.values():
        print(val)
    # Key Value両方
    for key, value in dict.items():
        print(key, value)
print('Traversing through a dictionary')
traverse_dict(edy)

# Search for an element in dictionary
def search_dict(dict, value):
    for key in dict:           # O(n)
        if dict[key] == value: # O(1)
            return key, value  # O(1)
    return 'The value does not exist'
print('Search for an element in dictionary')
print(search_dict(edy, 30))

# Delete an element from dictionary
print('Delete an element from dictionary')
del edy['age']
print(edy)
remove_element = edy.pop('address', None)
# popitem()は最後の要素を消す
# clear()はすべての要素を消す
print(remove_element)
print(edy)

# Dictionary method
print('Dictionary method')
bob = {'name': 'bob', 'age': 26, 'gender': 'male', 'address': 'NY'}
bob_two = bob.copy()
print(bob_two) # {'name': 'bob', 'age': 26, 'gender': 'male', 'address': 'NY'} shallow copy
bob_two.clear() # {}
new_dict = {}.fromkeys([1,2,3], 0) # {1: 0, 2: 0, 3: 0}
print(bob.get('age', 30)) # keyの値がなかったら、default値が返る
print(bob.items())        # dict_items([('name', 'bob'), ('age', 26), ('gender', 'male'), ('address', 'NY')])
print(bob.keys())         # dict_keys(['name', 'age', 'gender', 'address'])
print(bob.popitem())      # ('address', 'NY')
print(bob)                # {'name': 'bob', 'age': 26, 'gender': 'male'}
bob.setdefault('address', 'NY')
print(bob)                # {'name': 'bob', 'age': 26, 'gender': 'male', 'address': 'NY'}
print(bob.values())       # dict_values(['bob', 26, 'male', 'NY'])
num = {'a': 1, 'b': 2}
bob.update(num)
print(bob)                # {'name': 'bob', 'age': 26, 'gender': 'male', 'address': 'NY', 'a': 1, 'b': 2}

# Dictionary operation / builtin functions
print('Dictionary operation / builtin functions')
num = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6}
print('one' in num) # true
print(len(num))     # 6

# dictionary comprehension
print('dictionary comprehension')
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if condition}
city_names = ['paris', 'london', 'rome', 'berlin', 'madrid']
new_cities = {city: random.randint(20,30) for city in city_names}
print(new_cities)
temp_cities = {city: temp for (city, temp) in new_cities.items() if temp > 25}
print(temp_cities)
