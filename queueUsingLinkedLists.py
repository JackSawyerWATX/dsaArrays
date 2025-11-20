class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.front= None
    self.rear = None
    self.length = 0

  def enqueue(self, element):
    new_node = Node(element)
    if self.rear is None:
      self.front = self.rear = new_node
      self.length += 1
      return
    self.rear.next = new_node
    self.rear = new_node
    self.length += 1

  def dequeue(self):
    if self.isEmpty():
      return "Queue is empty (dequeue_)"
    temp = self.front
    self.front = temp.next
    self.length -= 1
    if self.front is None:
      self.read = None
    return temp.data

  def peek(self):
    if self.isEmpty():
      return "Queue is empty (peek_)"
    return self.front.data

  def isEmpty(self):
    return self.length == 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.front
    while temp:
      print(temp.data, end=".")
      temp = temp.next
    print()

myQueue = Queue()

myQueue.enqueue("Item 1")
myQueue.enqueue("Item 2")
myQueue.enqueue("Item 3")

print("Queue:", end="")

myQueue.printQueue()

print("Dequeued: ", myQueue.dequeue())
print("Peek: ", myQueue.peek())
print("isEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())



# =============================================================================
# DETAILED CODE EXPLANATION
# =============================================================================

# Node class represents individual elements in the linked list
# - self.data stores the actual value (could be any data type)
# - self.next points to the next node in the list (initially None)

# Queue class implements FIFO (First In, First Out) data structure using linked lists
# - self.front points to the first node (front of queue)
# - self.rear points to the last node (back of queue)
# - self.length tracks the number of elements for efficient size queries

# enqueue(element) - Add elements to the back of the queue (O(1) time)
# - Creates a new Node with the given element
# - If queue is empty, both front and rear point to the new node
# - Otherwise, link current rear to new node and update rear pointer
# - Increment length counter for efficient size tracking

# dequeue() - Remove and return the front element (O(1) time)
# - Check if queue is empty first to prevent errors
# - Store reference to current front node before removing
# - Move front pointer to the next node
# - Decrement length counter
# - If queue becomes empty, set rear to None too
# - Return the data from the removed node

# peek() - View the front element without removing it (O(1) time)
# - Check if queue is empty first
# - Return the data from the front node without modifying the queue

# isEmpty() - Check if queue is empty using the length counter (O(1) time)
# - More efficient than checking if front is None

# size() - Return the current size of the queue (O(1) time)
# - Uses the length counter instead of traversing the list

# printQueue() - Print all queue elements from front to rear
# - Start from front node and traverse to the end
# - Print each node's data with dot separator
# - Print newline at the end for clean output

# Usage example demonstrating queue operations:
# 1. Create a new Queue instance
# 2. Add three items using enqueue
# 3. Display all queue elements
# 4. Remove and display the front item (dequeue)
# 5. Show the new front item without removing it (peek)
# 6. Check if queue is empty
# 7. Display current queue size

# Key Concepts Demonstrated:
# - Linked List Structure: Each node contains data and a reference to the next node
# - FIFO Behavior: Elements added to rear, removed from front
# - Pointer Management: Front and rear pointers track queue boundaries
# - Edge Cases: Handling empty queue operations
# - Memory Efficiency: O(1) enqueue/dequeue operations
# - Length Tracking: Efficient size queries without traversal


