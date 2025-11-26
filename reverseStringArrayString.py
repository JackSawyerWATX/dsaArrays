def reverse(string):
  if len(string) == 0:
    return string
  reversed = " "

  for i in range(len(string) - 1, -1, -1):
    reversed += string[i]
  return reversed

print(reverse("The Late Show with David Letterman"))