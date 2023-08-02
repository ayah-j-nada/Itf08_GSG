def add(a,b):
    return a + b
def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a/b

def calc():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Sum:", add(num1, num2))
    print("subtraction", subtraction(num1, num2))
    print("Product:", multiplication(num1, num2))
    print("Division:", division(num1, num2))

calc()