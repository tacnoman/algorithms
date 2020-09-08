class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, capacity = 5):
        self.dummy_head = Node(None)
        self.dummy_tail = Node(None)

        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

        self.capacity = capacity
        self.size = 0


    def get_node(self, index):
        if index < self.size / 2:
            node = self.dummy_head.next
            while index > 0:
                node = node.next
                index -= 1
            return node
        else:
            node = self.dummy_tail.prev
            index = self.size - index
            while index > 0:
                node = node.prev
                index -= 1
            return node


    def move_to_front(self, key):
        node = self.dummy_head

        while node != None:
            node = node.next
            if node.value == key:
                node.prev.next = node.next
                node.next.prev = node.prev

                node.prev = self.dummy_head
                node.next = self.dummy_head.next

                self.dummy_head.next.prev = node
                self.dummy_head.next = node
                break


    def remove(self, i):
        node = self.get_node(i)
        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

        return node


    def remove_last(self):
        return self.remove(self.size)


    def put(self, index):
        node = Node(index)
        node.prev = self.dummy_head
        node.next = self.dummy_head.next
        self.dummy_head.next = node
        node.next.prev = node

        self.size += 1

        if self.size > self.capacity:
            return self.remove_last()
        return None


class Cache:
    def __init__(self, size = 5):
        self.cache = {} # Hashtable
        self.size = size
        self.dl_list = DoubleLinkedList(size)


    def put(self, key, value):
        if self.cache.get(key, None):
            self.dl_list.move_to_front(key)
        else:
            key_to_remove = self.dl_list.put(key)
            if key_to_remove:
                print("Removed key: " + key_to_remove.value)
                self.cache.pop(key_to_remove.value)

        self.cache[key] = value


    def get(self, key):
        return self.cache.get(key, None)


cache = Cache(2)
cache.put('v0', 2)
cache.put('v1', 2)
cache.put('v0', 3)
cache.put('v2', 2)
cache.put('v3', 2)
