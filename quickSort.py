def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]

  array[i + 1], array[high] = array[high], array[i + 1]
  return i + 1

def quickSort(array, low = 0, high = None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivotIndex = partition(array, low, high)
    quickSort(array, low, pivotIndex - 1)
    quickSort(array, pivotIndex + 1, high)

array = [19, 46, 82, 91, 37, 64, 28, 73, 55]
quickSort(array)

print(array)

# 1. Start with an unsorted array
# 2. Call quickSort with low=0 and high=len(array)-1 (full array range)
# 3. If low < high, proceed with partitioning; otherwise, subarray is sorted
# 4. Partition step: Select pivot (usually last element: 55)
# 5. Initialize i = low - 1 (-1 initially)
# 6. Iterate j from low to high-1, comparing each element with pivot
# 7. If array[j] <= pivot, increment i and swap array[i] with array[j]
# 8. After loop, swap pivot (array[high]) with array[i+1] to place pivot in correct position
# 9. Return pivot index (i+1) - elements left of pivot are smaller, right are larger
# 10. Recursively sort left subarray: quickSort(array, low, pivotIndex - 1)
# 11. Recursively sort right subarray: quickSort(array, pivotIndex + 1, high)
# 12. Base case: when low >= high, subarray has 0 or 1 elements (already sorted)
# 13. Process continues until all subarrays are sorted
# 14. Print the final sorted array


def partition2(array, low, high):
  pivot = len(array) / 2
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i += 1
      array[i], array[j] = array[j], array[i]
      return i + 1
    
def quicksort1(array, low = 0, high = None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivotIndex = partition(array, low, high)
    quicksort1(array, low, pivotIndex - 1)
    quicksort1(array, pivotIndex + 1, high)

array = [678, 345, 789, 123, 890, 234, 901, 456, 567]
quicksort1(array)
print(array)


# this algo chooses the middle of the array to be to be the pivot
# by choosing the length of the array and dividing it in half. This
# resulted in a faster running algo.