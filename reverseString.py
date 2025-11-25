def reverse(string):
  if len(string) == 0:
    return string
  reversed = " "

  for i in range(len(string) - 1, -1, -1):
    reversed += string[i]
  return reversed 

print(reverse("The Late Show with David Letterman"))

# 1. Start with a string
# 2. Initialize the string with " "
# 3. Iterate over string in reverse order
# 4. Append each character to the end of the string
# 5. Return the reversed string
# 6. Print the reversed string