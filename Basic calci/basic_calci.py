#basic_Math_Calculator

num1 = float(input("Enter the first number: "))
print("#Use '+','-','/','*'")
op = input("Enter the operator:   ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else :
    print("INVALID OPERATOR !!")
