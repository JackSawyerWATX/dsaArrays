stack = []

stack.append("A")
stack.append("B")
stack.append("C")
print(stack)

element = stack.pop()
print(stack)

stack.append("D")
print(stack)

topElement = stack[-1]
print(topElement)

isEmpty = not bool(stack)
print(isEmpty)

print(len(stack))



#    Push: Adds a new element on the stack by using append().
#    Pop: Removes and returns the top element from the stack using pop().
#    Peek: Returns the top element on the stack Ex. line 14 & 15.
#    isEmpty: Checks if the stack is empty Ex. line 17 & 18.
#    Size: Finds the number of elements in the stack len(stackArray).

