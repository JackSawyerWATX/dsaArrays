testArray = [9, 45, 99, 81, 90, 18, 36, 108, 63, 27, 72, 54]

def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left = mergeSort(arr[:mid])
  right = mergeSort(arr[mid:])

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

print("Original:", testArray)
print("Sorted:", mergeSort(testArray))


# Step-by-step explanation of Merge Sort algorithm:
# 1. Start with unsorted array: [9, 45, 99, 81, 90, 18, 36, 108, 63, 27, 72, 54]
# 2. Call mergeSort on the full array
# 3. Check base case: if array length <= 1, return (already sorted)
# 4. Calculate midpoint: mid = len(arr) // 2 = 5
# 5. Recursively split into left half: arr[:mid] = [9, 45, 99, 81, 90]
# 6. Recursively split into right half: arr[mid:] = [18, 36, 108, 63, 27, 72, 54]
# 7. Continue recursively splitting each half until single elements remain
# 8. Begin merging: start with smallest subarrays (single elements)
# 9. Compare elements from left and right subarrays
# 10. Append smaller element to result array, increment its index
# 11. Continue until one subarray is exhausted
# 12. Extend result with remaining elements from the other subarray
# 13. Return merged result up the recursion chain
# 14. Continue merging larger and larger sorted subarrays
# 15. Final merge combines the two main halves into fully sorted array
# 16. Return complete sorted array: [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99, 108]

# Key characteristics:
# - Divide and conquer algorithm
# - Stable sort (preserves relative order of equal elements)
# - Time complexity: O(n log n) in all cases
# - Space complexity: O(n) due to merge operations
# - Not in-place (requires additional memory)