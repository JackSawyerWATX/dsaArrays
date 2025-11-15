def countingSort(array):
  if not array:
    return array
  
  maxValue = max(array)
  count = [0] * (maxValue + 1)

  for number in array:
    count[number] += 1
  array[:] = []

  for number, frequency in enumerate(count):
    array.extend([number] * frequency)
      
  return array
    
unsortedArray = [19, 46, 82, 91, 37, 64, 28, 73, 55]
sortedArray = countingSort(unsortedArray)
print(sortedArray)


# Step-by-step explanation of Counting Sort algorithm:
# 1. Start with an unsorted array: [19, 46, 82, 91, 37, 64, 28, 73, 55]
# 2. Check if the array is empty; if so, return it (not the case here)
# 3. Find the maximum value in the array (91)
# 4. Create a count array of size maxValue + 1 (92 elements), initialized to 0
# 5. Iterate through each number in the input array and increment its count in the count array
# 6. Clear the original array to prepare for sorted output
# 7. Iterate through the count array using enumerate to get number and its frequency
# 8. For each number, extend the original array by adding the number frequency times
# 9. Return the sorted array
# 10. Print the final sorted array: [19, 28, 37, 46, 55, 64, 73, 82, 91]

# Key features of Counting Sort:
# - Efficient for sorting integers within a known range
# - Non-comparative sorting algorithm
# - Time complexity: O(n + k), where n is number of elements and k is range of input

