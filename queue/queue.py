import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, item):
        self.storage.add_to_head(item)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return None
        popped_item = self.storage.remove_from_tail()
        self.size -= 1
        return popped_item

    def len(self):
        return self.size
