class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedDictionary:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        new_node = Node(key, value)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):
        current = self.head
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False


class HashDictionary:
    def __init__(self, size=256):
        self.size = size
        self.table = [LinkedDictionary() for _ in range(size)]

    def hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        i = self.hash(key)
        self.table[i].insert(key, value)

    def search(self, key):
        i = self.hash(key)
        return self.table[i].search(key)

    def delete(self, key):
        i = self.hash(key)
        return self.table[i].delete(key)


h = HashDictionary()

h.insert("apple", 10)
h.insert("banana", 20)
h.insert("grape", 30)

print(h.search("apple"))   # 10
print(h.search("banana"))  # 20

h.delete("banana")
print(h.search("banana"))  # None