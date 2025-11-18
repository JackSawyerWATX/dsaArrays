queue = []

queue.append("Pork")
queue.append("Chop")
queue.append("Sand")
queue.append("Wiches")
print("Initial queue:", queue)

firstItem = queue[0]
print("First item in queue:", firstItem)

poppedElement = queue.pop(0)
print("Dequeued item:", poppedElement)
print("Queue after dequeue:", queue)

queue.append("Pickles")
print("Queue with new item added:", queue)

isEmpty = not bool(queue)
print("True or False: This queue is empty:", isEmpty)

print("How many items are in this queue?", len(queue))

