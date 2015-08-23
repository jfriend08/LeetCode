"""
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and all test cases.
"""

class Stack(object):
    def __init__(self):
      self.myQ = []

    def push(self, x):
      self.myQ.insert(0,x)

    def pop(self):
      if self.myQ:
        self.myQ.pop(0)

    def top(self):
      return self.myQ[0]

    def empty(self):
      if self.myQ:
        return False
      return True
    def pQ(self):
      print self.myQ

if __name__ == "__main__":
  test = Stack()
  test.push(1)
  test.pQ()
  test.push(2)
  test.pQ()
  test.pop()
  test.pQ()
  test.top()
  test.pQ()

