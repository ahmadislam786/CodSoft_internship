#TASK-2 PERFORM BASIC ARITHMETIC OPERATIONS BASED ON THE GIVEN OPERATION

def switch(operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
while True: 
    num1 = int(input("Enter first integer:"))
    num2 = int(input("Enter Second integer:"))
    operator = input("Enter the operation to perform (+, -, *, /):")
    result = switch(operator)
    print(f"{num1} {operator} {num2} = {result}")
    again=input("Do you wants more calculation(yes/no):").lower()
    if "no" in again:
        break
print("Thank you!")
