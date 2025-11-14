array = [19, 46, 82, 91, 37, 64, 28, 73, 55]

n = len(array)
for i in range(n):
  minimumIndex = i
  for j in range(i + 1, n):
    if array[j] < array[minimumIndex]:
      minimumIndex = j
  array[i], array[minimumIndex] = array[minimumIndex], array[i]

print(array)

# 1. Start with an unsorted array
# 2. Set n equal to the length of the array (9 elements)
# 3. Begin outer loop: for i in range(n) - this will iterate through each position
# 4. For each position of i, assume it's the minimum (minimumIndex = i)
# 5. Begin inner loop: for j in range(i + 1, n) - search remaining elements
# 6. Compare array[j] with array[minimumIndex] - find smaller element
# 7. If smaller element found, update minimumIndex to j
# 8. After inner loop completes, swap array[i] with array[minimumIndex]
# 9. Move to next position (i + 1) and repeat steps 4-8
# 10. Continue until entire array is sorted
# 11. Print the final sorted array

