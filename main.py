
#function to add
def add(num1, num2):
    num3 = num1 + num2
    return num3

#function to subtract
def subtract(num1, num2):
    num3 = num1 - num2
    return num3

#function to divide
def divide(num1, num2):
    num3 = num1/num2
    return num3

#function to multiply
def multiply(num1, num2):
    num3 = num1*num2
    return num3

print("Choose operator")
print("Choose 1 for adding two numbers")
print("Choose 2 for substract two numbers")
print("Choose 3 for divide two numbers")
print("Choose 4 for multiply two numbers")

choice = int(input())

print("Enter first number: ")
num1 = int(input())

print("Enter second number: ")
num2 = int(input())

if choice == 1:
    print("Result:  ", add(num1, num2))
elif choice == 2:
    print("Result: ",subtract(num1, num2))
elif choice == 3:
    print("Result: ", divide(num1, num2))
elif choice == 4:
    print("Result: ", multiply(num1, num2))
else:
    print("Invalid operator")
