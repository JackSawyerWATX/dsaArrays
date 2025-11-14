array = [19, 46, 82, 91, 37, 64, 28, 73, 55]

n =  len(array)
for i in range(1, n):
  insertIndex = i
  currentValue = array.pop(i)
  for j in range(i - 1, -1, -1):
    if array[j] > currentValue:
      insertIndex = j
  array.insert(insertIndex, currentValue)

print(array)

# 1. Start with an unsorted array
# 2. Set n equal to the length of the array (9 elements)
# 3. Begin outer loop: for i in range(1, n) - start from second element (index 1)
# 4. Set insertIndex to current position i
# 5. Remove and store the current element at position i using pop(i)
# 6. Begin inner loop: for j in range(i - 1, -1, -1) - iterate backwards through sorted portion
# 7. Compare each element in sorted portion with currentValue
# 8. If element > currentValue, update insertIndex to j (shift position left)
# 9. After finding correct position, insert currentValue at insertIndex
# 10. Move to next element (i + 1) and repeat steps 4-9
# 11. Continue until all elements are inserted into correct positions
# 12. Print the final sorted array