import sys
sys.path.append('doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = []

  def push(self, value):
        self.storage.append(0, value)
        self.size += 1
  
  def pop(self):
    if len(self.storage) == 0:
      return None
    else:
      return self.storage.pop()

  def len(self):
    return len(self.storage)
