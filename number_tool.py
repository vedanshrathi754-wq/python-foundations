print("Number Utility Tool")
print("1. check even or odd ")
print("2. find factorial")
print("3. sum of digits")

choice = int(input("Enter your choice(1-3): "))
num = int(input("Enter a number:"))

if choice ==1:
  if num % 2 ==0:
    print("Even number")
  else:
    print("Odd number")

elif choice == 2:
  fact = 1
  for i in range(1,num + 1):
    fact*=i
  print("Factorial:", fact)

elif choice == 3:
  s = 0
  while num > 0:
    s += num % 10
    num //= 10
  print("Sum of digits:", s )

else:
  print("Invalid choice")
