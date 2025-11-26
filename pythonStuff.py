print ("Hello Python")

a = 2 + 3
print(a)

print ((5 * 7) / (2 + 3))

def functionOne (a, b):
  return a * b
print (functionOne(5, 6))

def functionTwo():
  a = 26
  if a >= 22:
    return("It's too much.")
  elif a == 20:
    return("That's it!")
  else:
    return("Not enough.")
  
print(functionTwo())

for i in range(10):
  print("For Loop:", i)

print("~~~~~~~~~~~~~~~~NEXT~~~~~~~~~~~~~~~~")

j = 1
while j <= 10:
  print("While Loop:", j)
  j += 1

sampleList=["a", "b", "c", "d", "e", "f", "g", 'h', 'i', "j", "k"]
print(sampleList)
print(sampleList[2:6])
print(sampleList[5:7])
sampleList.extend(["l", "m", "n", "o"])
print(sampleList)
sampleList.append("p")
print(sampleList)
sampleList[9] = 'J'
sampleList[14] = 'O'
sampleList[13] = 'N'
print(sampleList)
sampleList.pop()
print(sampleList)
sampleList.reverse()
print(sampleList)
sampleList.sort()
print(sampleList)


person = {
  "fname": "Jack",
  "lname": "Sawyer",
  "age": 45,
  "address":
  {
    "houseNumber": 403,
    "street": "SE 227th Street",
    "city": "Redmond",
    "state": "Washington",
    "postalCode": "WA",
    "ZIP": 98021
  },
  "gender": "Sasquach",
  "isEmployed": True,
  "profession": "Squrrell",
  "hobbies": ["reading", "hiking", "biking", "cooking", "gaming"],
  "spouse": None,
}

fullName = person["fname"] + " " + person["lname"]

print(person["fname"], person["lname"])
print(fullName)
print(person["address"]["houseNumber"], person["address"]["street"])
print(person["address"]["city"] + ", " + person["address"]["postalCode"] + " " + str(person["address"]["ZIP"]))

