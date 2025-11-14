array = [19, 46, 82, 91, 37, 64, 28, 73, 55]

n =  len(array)
for i in range(1, n):
  insertIndex = i
  currentValue = array(i)
  for j in range(i - 1, -1, -1):
    if array[j] > currentValue:
      array[j + 1] = array[j]
      insertIndex = j
    else:
      break
  array[insertIndex] = currentValue

print(array)



# Step-by-step explanation of Improved Insertion Sort algorithm:
# 1. Start with an unsorted array: [19, 46, 82, 91, 37, 64, 28, 73, 55]
# 2. Set n equal to the length of the array (9 elements)
# 3. Begin outer loop: for i in range(1, n) - start from second element (index 1)
# 4. Set insertIndex to current position i
# 5. Store currentValue as array[i] (no removal needed - in-place operation)
# 6. Begin inner loop: for j in range(i - 1, -1, -1) - iterate backwards through sorted portion
# 7. Compare array[j] with currentValue
# 8. If array[j] > currentValue: shift element right (array[j + 1] = array[j]) and update insertIndex
# 9. If array[j] <= currentValue: break early (optimization - no need to check further left)
# 10. After inner loop, place currentValue at correct position: array[insertIndex] = currentValue
# 11. Move to next element (i + 1) and repeat steps 4-10
# 12. Continue until all elements are in correct positions
# 13. Print the final sorted array
#
# Key improvements over basic insertion sort:
# - In-place shifting instead of pop/insert operations (more efficient)
# - Early termination with break when correct position found
# - Direct array access without modifying array structure during sorting
# - Better performance on partially sorted arrays due to early break