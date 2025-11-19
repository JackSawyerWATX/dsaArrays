class Stack:
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.items.pop()
  
  def peek(self):
    if self.isEmpty():
      return "Stack is empty."
    return self.items[-1]

  def isEmpty(self):
    return len(self.items) == 0
  
  def size(self):
    return len(self.items)


myStack = Stack()

myStack.push("First")
myStack.push("Second")
myStack.push("Third")

print(myStack.items)

print(myStack.pop())

print(myStack.peek())

print(myStack.isEmpty())

print(myStack.size())