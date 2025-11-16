array = [274, 850, 105, 627, 391, 925, 527, 793, 486, 1025, 1107, 1256]
print("Original array:", array)
radixArray = [[],[],[],[],[],[],[],[],[],[]]

maxValue = max(array)
exp = 1

while maxValue // exp > 0:
  while len(array) > 0:
    val = array.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      array.append(val)

  exp *= 10

print("Sorted array:", array)


# 1. Start with an unsorted array.
# 2. Initialize radixArray with 10 empty buckets (one for each digit 0-9)
# 3. Find maxValue to determine how many digits we need to process
# 4. Set exp = 1 (start with units place/ones digit)
# 5. Begin outer while loop: while maxValue // exp > 0 (continue until we've processed all digits)
# 6. Begin distribution phase: while array still has elements
# 7. Remove last element from array using pop() (works like a stack)
# 8. Calculate radixIndex = (val // exp) % 10 to get the current digit being processed
# 9. Append the value to the appropriate bucket based on its current digit
# 10. After all elements are distributed, begin collection phase
# 11. For each bucket in radixArray (iterate through buckets 0-9)
# 12. While bucket has elements, pop from bucket and append back to main array
# 13. This maintains stability - elements with same digit stay in original relative order
# 14. After all buckets are collected, multiply exp by 10 to move to next digit place
# 15. Repeat steps 5-14 for tens place, hundreds place, etc. until all digits processed
# 16. Final result: array is now sorted in ascending order

# Key characteristics:
# - Stable sort algorithm that maintains relative order of equal elements
# - Non-comparison based algorithm
# - Time complexity: O(d * (n + b)) where d is digits, n is elements, b is buckets (10)
# - Space complexity: O(n + b) for the additional bucket space
# - Most efficient when range of numbers is limited but numbers have many digits

