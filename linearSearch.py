def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

arr = [4, 9, 1, 7, 0, 6, 3, 8, 2, 5]
targetVal = 7

result = linearSearch(arr, targetVal)

if result != -1:
  print("Value", targetVal, "found at index", result)
else:
  print("Value", targetVal, "not found in the array")