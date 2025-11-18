import time
import winsound

zero = 0
one = 1

print(zero)
winsound.Beep(800, 100)  # 800 Hz frequency, 100 ms duration
print(one)
winsound.Beep(800, 100)  # 800 Hz frequency, 100 ms duration


for fibbo in range (18):
  newFibbo = one + zero

  print(newFibbo)
  zero = one
  one = newFibbo



nothing = 0
something = 1

for fibsy in range (10): # this is how many times it will iterate, not the top number it will go to.
  flaps = nothing + something

  print(flaps)
  time.sleep(.025)

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


x = [13, 17, 14, 18, 15, 12, 16,]
x.append(19)
print(x)
x.sort()
print(x)