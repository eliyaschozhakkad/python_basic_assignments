class MathOperation:
    def addition(self, x, y):
        return x + y

    def subtraction(self, x, y):
        return x - y

    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        return x / y


operation = MathOperation()
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
inp = int(input("Enter the option : "))
number1 = int(input("Enter first number"))
number2 = int(input("Enter second number"))
result = 0
match inp:
    case 1:
        result = operation.addition(number1, number2)
    case 2:
        result = operation.subtraction(number1, number2)
    case 3:
        result = operation.multiplication(number1, number2)
    case 4:
        result = operation.division(number1, number2)
    case _:
        print("Invalid Entry")
print(f"The result is {result}")
