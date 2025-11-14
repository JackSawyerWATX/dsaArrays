array = [19, 46, 82, 91, 37, 64, 28, 73, 55]

n = len(array)
for i in range(n - 1):
  minimumIndex = i
  for j in range(i + 1, n):
    if array[j] < array[minimumIndex]:
      minimumIndex = j
  minimumValue = array.pop(minimumIndex)
  array.insert(i, minimumValue)

print(array)