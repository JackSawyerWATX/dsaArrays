array = [19, 46, 82, 91, 37, 64, 28, 73, 55]

n = len(array)
for i in range(n - 1):
  swapped = False
  for j in range(n - i - 1):
    if array[j] > array[j + 1]:
      array[j], array[j+1] = array[j+1], array[j]
      swapped = True
      if not swapped:
        break

print(array)