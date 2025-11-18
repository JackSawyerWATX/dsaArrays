class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
      self.queue.append(item)

  def dequeue(self):
      if self.isEmpty():
        return "queue is empty"
      return self.queue.pop(2)

  def peek(self):
      if self.isEmpty():
        return "Queue is Empty"
      return self.queue[0]
    
  def isEmpty(self):
      return len(self.queue) == 0
    
  def size(self):
      return len(self.queue)
    
myQueue = Queue()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")
myQueue.enqueue("D")


print("Queue:", myQueue.queue)
print("Peek:", myQueue.peek())
print("Queue:", myQueue.queue)
print("Dequeue:", myQueue.dequeue())
print("Queue:", myQueue.queue)
print("Queue after queue:", myQueue.queue)
print("isEmpty:", myQueue.isEmpty())
print("Size:", myQueue.size())

