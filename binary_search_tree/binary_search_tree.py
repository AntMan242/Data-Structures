# import sys
# sys.path.append('../queue_and_stack')
# from queue import Queue
# from stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = BinarySearchTree(value)
    # if value is less than self.value
    if value < self.value:
      # check if left is none
      if self.left == None:
        # if none, set left to be this node
        self.left = node
        # if not, call the left node's insert with this value
      else:
        self.left.insert(value)

    else:
      # if value is >= to self.value
      if value >= self.value:
        # check if right side is none
        if self.right == None:
          # if none, set right to be node
          self.right = node
          # if node is there, call self.right.insert with this value
        else:
          self.right.insert(value)

  def contains(self, target):
    # if self.value is the target
    if self.value == target:
      return True

    #if the target is less than self.value
    if target < self.value:
      # check if there's a left side
      if self.left:
        # if yes, return left.contains on the target
        return self.left.contains(target)
        # if not, return false
      else:
        return False
    else:
      # otherwise the target must be greater than self.value
      if target > self.value:
        # check if right side exists
        if self.right:
          # if yes, return self.right.contains on the target
          return self.right.contains(target)
          # if not, return false
        else:
          return False

  def get_max(self):
    # if we have a right
    if self.right:
      # return the max on the right
      return self.right.get_max()
      # otherwise return self.value
    else:
      return self.value

  def for_each(self, cb):
    # callback on the self's value
    cb(self.value)

    #if self.right
    if self.right:
      # call the right for_each with the cb
      self.right.for_each(cb)

    # if self.left
    if self.left:
      # call left for_each with the cb
      self.left.for_each(cb)