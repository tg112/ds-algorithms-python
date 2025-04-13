from asyncio import new_event_loop


class Node:
    def __init__(self, value):
        self.value = value # O(1)
        self.next = None   # O(1)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # print linked list
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    # insert an element at the end
    def append(self, value): # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # insert an element at the beginning
    def prepend(self, value): # O(1)
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # insert an element in the middle
    def insert(self, value, index): # O(1) or O(n)
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1): # O(n)
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    # traverse
    def traverse(self): # O(n)
        current = self.head # O(1)

        while current is not None: # O(n)
            print(current.value)
            current = current.next

    # search
    def search(self, target): # O(N)
        current = self.head
        index = 0
        while current: # O(N)
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1

    # get an element where the index is
    def get(self, index):
        if index == -1:
            return self.tail.value
        if index < 0 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    # set an element where the index is
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    # pop first
    def pop_first(self):       # O(1)
        popped_node = self.head
        if self.length == 0:   # O(1)
            return None
        elif self.length == 1: # O(1)
            self.head = None
            self.length = None
        else:                  # O(1)
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    # pop last
    def pop(self): # O(n)
        popped_node = self.tail
        if self.length == 0:   # O(1)
            return None
        elif self.length == 1: # O(1)
            self.head = None
            self.tail = None
        else:                  # O(n)
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp.next = None
            self.length -= 1
            return popped_node

    # remove a node on the index position
    def reomove(self, index): # O(n)
        if index >= self.length or index < -1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 or index == -1:
            return self.pop()           # O(n)
        prev_node = self.get(index - 1) # O(n)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1

    # delete all nodes
    def delete_all(self): # O(1)
        self.head = None
        self.tail = None
        self.length = 0
        return None


linkedList = LinkedList()
linkedList.insert(-1, 0)
linkedList.append(10)
linkedList.append(20)
linkedList.append(30)
linkedList.prepend(0)
linkedList.insert(100, 2)
# linkedList.traverse()
print(linkedList.get(-1))
linkedList.set_value(2, 1000)
linkedList.pop_first()
linkedList.pop()
linkedList.reomove(1)
print(linkedList.search(10))
print(linkedList)
linkedList.delete_all()
print(linkedList)
