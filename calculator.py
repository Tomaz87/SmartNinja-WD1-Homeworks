# simple calculator

number_one = int(input("Insert the first number: "))
number_two = int(input("Insert the second number: "))

x = number_one
y = number_two

operation = input("Chose math operation (+, -, *, /):")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Choose math operation according to instructions.")