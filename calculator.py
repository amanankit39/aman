num1 = float(input("Enter the number : "))  # store the first number
op = input("Enter the operator (+, -, *, /) : ")    # store the operator
num2 = float(input("Enter the number : "))  # store the second number

def calculator(num1, op, num2):
    # add the numbers
    if op == "+":
        return num1 + num2
    # subtract the numbers
    elif op == "-":
        return num1 - num2
    # multiply the numbers
    elif op == "*":
        return num1 * num2
    # divide the number if divisor is not zero
    elif op == "/":
        if num2 == 0:
            raise ValueError("Can't divide a number by zero")
        else:
            return num1 / num2
    # if the user enters the invalid operator then print the error message
    else:
        raise ValueError("Invalid Opertor")

if __name__ == "__main__":
    print(calculator(num1, op, num2))
