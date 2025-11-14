array = [19, 46, 82, 91, 37, 64, 28, 73, 55]

n = len(array)

for i in range(n - 1):
  for j in range(n - i - 1):
    if array[j] > array[j + 1]:
      array[j], array[j + 1] = array[j + 1], array[j]

print(f"The length of the array is {n}.")
print(f"The array is {', '.join(map(str, array))}")

# 1.  Creates a variable that is n that is the length of the array.
#     In this case, it's 8.
# 2.  Loops through the integer i for the length of the array, minus 1.
#     In this case its 8 - 1, or 7.
# 3.  Create another loop nested inside the pervious loop that iterates
#     variable n, in this case being the length of the array which = 8,
#     minus the current value of i, calcualted to 7, and then minus 1
#     from 7. This concludes that j compares item 6 to 7 in the array.
# 4.  If j is greater than j + 1, whatever j is plus 1, then we set the 
#     number geater than j to the left of j. This is done in what looks
#     to be backwards, but is assigning the larger number to the to the 
#     right of the smaller number because the algo starts sorting from
#     the right and works left.
# 5.  Finally, it prints the array.