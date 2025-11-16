unsortedArray = [9, 45, 99, 81, 90, 18, 36, 108, 63, 27, 72, 54]

def mergeSort(array):
  if len(array) <= 1:
    return array
  
  mid = len(array) // 2
  leftHalf = array[:mid]
  rightHalf = array[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

sortedArray = mergeSort(unsortedArray)

print(sortedArray)

# Step-by-step explanation of Merge Sort algorithm:
# 1. Start with an unsorted array.
# 2. Call mergeSort on the full array.
# 3. Check base case: if array length <= 1, return array (already sorted)
# 4. Calculate mid point: mid = len(array) // 2 (integer division)
# 5. Split array into two halves: leftHalf = array[:mid], rightHalf = array[mid:]
# 6. Recursively call mergeSort on leftHalf until it reaches base case
# 7. Recursively call mergeSort on rightHalf until it reaches base case
# 8. Call merge function with the two sorted halves
# 9. In merge function: Initialize empty result array and indices i=j=0
# 10. While both arrays have elements to compare:
#     - Compare left[i] and right[j]
#     - Append smaller element to result and increment its index
# 11. After comparison loop, extend result with remaining elements from left array (if any)
# 12. Extend result with remaining elements from right array (if any)
# 13. Return merged result array
# 14. Continue merging up the recursion tree until original array is fully sorted
# 15. Print the final sorted array
#
# Key characteristics of Merge Sort:
# - Divide and conquer algorithm
# - Stable sort (maintains relative order of equal elements)
# - Time complexity: O(n log n) for all cases (worst, average, best)
# - Space complexity: O(n) due to additional space for merging
# - Not in-place sorting (requires extra memory)
# - Excellent for large datasets and external sorting