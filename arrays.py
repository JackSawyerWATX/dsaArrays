array1 = [7, 12, 9, 4, 11]
print(array1)
print(len(array1))
print( array1[0] )

minVal = array1[0]
for i in array1:
  if i < minVal:
    minVal = array1[i]
    minVal = i

print(minVal)

maxVal = array1[0]
for i in array1:
  if i > maxVal:
    maxVal = i

print(maxVal + 1)