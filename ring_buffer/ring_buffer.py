from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()

    def append(self, item):
        # That's O(1)
        self.storage.add_to_tail(item)
        if len(self.storage) > self.capacity:
            # current is the position of the oldest element in the output list
            # starts at 0, then shifts by one every time we add something to buffer
            self.current = (self.current+1) % self.capacity
            self.storage.remove_from_head()

    def get(self):
        list_buffer_contents = []  # Note:  This is the only [] allowed
        # Behaves differently depending on whether it's full or not
        if len(self.storage) < self.capacity:
            next = self.storage.head
            for _ in range(len(self.storage)):
                list_buffer_contents.append(next.value)
                next = next.next
        else:
            next = self.storage.head
            # building output list in two passes, first, the oldest and all the elements 'current'
            # then, all the elements before 'current'
            for _ in range(self.current, self.capacity):
                list_buffer_contents.append(next.value)
                next = next.next
            for _ in range(0, self.current):
                list_buffer_contents.insert(
                    self.current-self.capacity, next.value)
                next = next.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    """
    Overall this seems like a straight up better version, since it has the same complexity for both operations
    and is much more concise and readable
    """
    def __init__(self, capacity):
        self.current = 0
        self.storage = [None] * capacity
        # the requirement for storage to have the length equal to capacity on initialization is pretty strange in my opinion 

    def append(self, item):
        self.storage[self.current] = item
        self.current = (self.current + 1) % len(self.storage)
        # appending here's is O(1)

    def get(self):
        # This is O(n) since we are shallow copying the array
        return [element for element in self.storage if element is not None]
