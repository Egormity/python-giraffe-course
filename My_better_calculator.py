
num1 = float(input("Enter your number: "))
op = input("Enter your operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
if op == "-":
    print(num1 - num2)
if op == "*":
    print(num1 * num2)
if op == "/":
    print(num1 / num2)
else:
    print("Entered an invalid operator")