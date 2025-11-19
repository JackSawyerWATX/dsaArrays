def linearSearch(array, targetVal):
  for i in range(len(array)):
    if array[i] == targetVal:
      return i
  return -1

array = [4, 9, 1, 7, 0, 6, 3, 8, 2, 5]
print("Unsorted array:", array)
targetVal = 6

result = linearSearch(array, targetVal)
array.sort()

print("Sorted array:", array)
print("Linear Search Results:")

if result != -1:
  print("Value", targetVal, "found at index", result)
else:
  print("Value", targetVal, "not found in the array")


