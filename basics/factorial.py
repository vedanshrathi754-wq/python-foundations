# Program to calculate factorial of a number
# Factorial of n = n * (n-1) * (n-2) ... * 1

n = int(input("Enter a number: "))

fact = 1  # variable to store factorial value

# Loop from 1 to n
for i in range(1, n + 1):
    fact = fact * i

print("Factorial:", fact)

