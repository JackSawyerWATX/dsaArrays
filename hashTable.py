array = [None] * 10

def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

def contains(name):
  index = hash_function(name)
  return array[index] == name

def add(name):
  index = hash_function(name)
  array[index] = name

add("Jones")
add("Brody")
add("Ravenwood")
add("Belloq")
add("Sallah")
add("Toht")

print(hash_function("Ravenwood"))

print(contains("Ravenwood"))
print(contains("Indiana"))

# 1. Creates an array of size 10, initialized to None values
# 2. Defines a hash_function that converts strings to hash indices (0-9)
# 3. Defines a contains function that checks if a name exists at its hash index
# 4. Defines an add function that stores names at their computed hash indices
# 5. Adds "Jones" to the hash table at index hash_function("Jones")
# 6. Adds "Brody" to the hash table at index hash_function("Brody")
# 7. Adds "Ravenwood" to the hash table at index hash_function("Ravenwood")
# 8. Adds "Belloq" to the hash table at index hash_function("Belloq")
# 9. Adds "Sallah" to the hash table at index hash_function("Sallah")
# 10. Adds "Toht" to the hash table at index hash_function("Toht")
# 11. Prints the hash value of "Ravenwood" (should be 9)
# 12. Tests contains("Ravenwood") - should return True since it was added
# 13. Tests contains("Indiana") - should return False since it was never added 