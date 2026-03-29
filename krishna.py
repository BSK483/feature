//////// CODE 1 is ready /////////

print("Hello, World!")

/////// CODE 2 Is ready //////////

# This program adds two numbers
# Input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Add two numbers
sum = num1 + num2
# Display the sum
print("The sum is:", sum)


////// CODE 3 i Ready //////////

# This program finds the square root of a number
import math
# Input from the user
num = float(input("Enter a number: "))
# Calculate square root
sqrt = math.sqrt(num)
# Display the result
print("The square root of", num, "is:", sqrt)

//// code 4 is ready /////
# This program checks if a number is prime
num = int(input("Enter a number: "))
if num > 1:
   for i in range(2, int(num/2)+1):
       if (num % i) == 0:
           print(num, "is not a prime number")
           break
   else:
       print(num, "is a prime number")
else:
   print(num, "is not a prime number")
