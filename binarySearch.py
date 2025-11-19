def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid
    
    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

array = [4, 9, 1, 7, 0, 6, 3, 8, 2, 5]
print(array)
array.sort()  # Sort the array before binary search
target = 7

result = binarySearch(array, target)

print("Sorted array:", array)
print("Binary Search Results:")

if result != -1:
  print("Value", target, "found at index", result)
else:
  print("Value", target, "not found in the array")


# Create an array - line 7
# Create a value to search for - line 9
# Create a loop that runs while the left index is less than or equal to the right 
#   index.
# Create an if statement at the end that checks the target value to be less than or 
#   larger than 
#   the middle value, then updates the left or right variables to narrow the search.
# Create an if statement compares the middle value to the target value and then
#   returns that value.
# After the loop, return -1 because at this point we know that the target has not 
#   been found.