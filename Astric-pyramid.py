num = int(input("Enter a no of rows"))
for x in range(0, 8):
  if (x % 2 == 0):
    for i in range(0, num):
      for j in range(0, i + 1):
        print(end=" ")
      for j in range(0, num - i):
        print("*", end=" ")
      print()
  else:
    for i in range(0, num):
      for j in range(0, num-i):
        print(end=" ")
      for j in range(0, i+1):
        print("*", end=" ")
      print()
