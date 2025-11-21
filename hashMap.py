class SimpleHashMap:
  def __init__(self, size=100):
    self.size = size
    self.buckets =[[] for _ in range(size)]

  def hash_function(self, key):
    numeric_sum = sum(int(char) for char in key if char.isdigit())
    return numeric_sum % 10
  
  def put(self, key, value):
    index = self.hash_function(key)
    bucket = self.buckets[index]
    for i, (k, v) in enumerate(bucket):
      if k == key:
        bucket[i] = (key, value)
        return
    bucket.append((key, value))

  def get(self, key):
    index = self.hash_function(key)
    bucket = self.buckets[index]
    for k, v in bucket:
      if k ==key:
        return v
    return None
  
  def remove(self, key):
    index = self.hash_function(key)
    bucket = self.buckets[index]
    for i, (k, v) in enumerate(bucket):
      if k == key:
        del bucket[i]
        return

  def print_map(self):
    print("Hash Map Contains: ")
    for index, bucket in enumerate(self.buckets):
      print(f"Bucket {index}: , {bucket}")

hash_map = SimpleHashMap(size=10)

hash_map.put("867-5313", "Jacky")
hash_map.put("867-5308", "Jamie")
hash_map.put("867-5315", "Jeffery")
hash_map.put("867-5309", "Jenny")
hash_map.put("867-5312", "Jerry")
hash_map.put("867-5311", "Jimmy")
hash_map.put("867-5310", "Johnny")
hash_map.put("867-5314", "Joey")

hash_map.print_map()

print("\nName associated with '867-5309':", hash_map.get("867-5309"))

print("Updating the name for '867-5311' to 'James'")
hash_map.put("867-5311", "James")

hash_map.print_map()

print(hash_map.get("867-5310"))



# 1. Create a list of buckets, each is a list to handle collisions
# 2. Add only the numerical values of the key, ignoring non-numeric characters
# 3. Perform modulo 10 on the sum
# 4. Add or update a key value pair
# 5. Update existing key
# 6. Add new key-value pair if not found
# 7. Retrieve value by key
# 8. Return None if key not found
# 9. Remove key-value pair by key
# 10. Print all buckets and their contents
# 11. Instantiate SimpleHashMap with 10 buckets
# 12. Add multiple phone number-name pairs to the hash map
# 13. Print the entire hash map
# 14. Retrieve and print the name associated with phone number '867-5309'
# 15. Update the name for phone number '867-5311' to 'James'
# 16. Print the updated hash map
# 17. Retrieve and print the name associated with phone number '867-5310'