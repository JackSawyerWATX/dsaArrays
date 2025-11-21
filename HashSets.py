class SimpleHashSet:
  def __init__(self, size=100):
    self.size = size
    self.buckets = [[] for _ in range(size)]

  def hash_function(self, value):
    return sum(ord(char) for char in value) % self.size
  
  def add(self, value):
    index = self.hash_function(value)
    bucket = self.buckets[index]
    if value not in bucket:
      bucket.append(value)

  def contains(self, value):
    index = self.hash_function(value)
    bucket = self.buckets[index]
    return value in bucket
  
  def remove(self, value):
    index = self.hash_function(value)
    bucket = self.buckets[index]
    if value in bucket:
      bucket.remove(value)

  def print_set(self):
    print("Hash set contents: ")
    for index, bucket in enumerate(self.buckets):
      print(f"Bucket {index}: {bucket}")

hash_set = SimpleHashSet(size=10)

hash_set.add("George Washington")
hash_set.add("John Adams")
hash_set.add("Thomas Jefferson")
hash_set.add("James Madison")
hash_set.add("James Monroe")
hash_set.add("John Quincy Adams")

print(hash_set.contains("Thomas Jefferson"))
print(hash_set.contains("Abraham Lincoln"))
hash_set.remove("John Adams")

hash_set.print_set()

# 1. Defines the SimpleHashSet class with an __init__ method that creates a list of empty buckets
# 2. Implements hash_function that converts strings to hash indices using character sum modulo size
# 3. Creates add() method that inserts values into appropriate buckets, avoiding duplicates
# 4. Creates contains() method that checks if a value exists in its corresponding bucket
# 5. Creates remove() method that deletes values from their buckets if they exist
# 6. Creates print_set() method that displays all buckets and their contents
# 7. Instantiates a SimpleHashSet object with size 10 (10 buckets)
# 8. Adds "George Washington" to bucket determined by hash_function("George Washington")
# 9. Adds "John Adams" to bucket determined by hash_function("John Adams")
# 10. Adds "Thomas Jefferson" to bucket determined by hash_function("Thomas Jefferson")
# 11. Adds "James Madison" to bucket determined by hash_function("James Madison")
# 12. Adds "James Monroe" to bucket determined by hash_function("James Monroe")
# 13. Adds "John Quincy Adams" to bucket determined by hash_function("John Quincy Adams")
# 14. Prints True/False result of checking if "Thomas Jefferson" is in the hash set
# 15. Prints True/False result of checking if "Abraham Lincoln" is in the hash set
# 16. Removes "John Adams" from its bucket in the hash set
# 17. Calls print_set() to display the contents of all buckets, showing hash collisions