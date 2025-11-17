import time
import winsound

zero = 0
one = 1

print(zero)
print(one)

for fibbo in range (18):
  newFibbo = one + zero

  print(newFibbo)
  winsound.Beep(800, 100)  # 800 Hz frequency, 100 ms duration
  zero = one
  one = newFibbo



nothing = 0
something = 1

for fibsy in range (1000): # this is how many times it will iterate, not the top number it will go to.
  flaps = nothing + something

  print(flaps)
  time.sleep(0.0001)

  nothing = something
  something = flaps





def flapper(n):
  if n <= 1:
    return n
  else:
    return flapper(n-1) + flapper(n-2)

print("+-------------------")
print("| ",flapper(20))
print("+-------------------")
