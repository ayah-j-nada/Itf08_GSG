def add():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return print(f"{num1} + {num2} = {num1 + num2}")


def subtract():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return print(f"{num1} - {num2} = {num1 - num2}")


def multiply():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    return print(f"{num1} * {num2} = {num1 * num2}")


def division():
    while True:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if num2 == 0:
            print("Cannot divide by zero. Please enter a non-zero second number. ")
            continue
        else:
            return print(f"{num1} / {num2} = {num1 / num2}")


def triangle_area():
    while True:
        base = int(input("Enter the base length of the triangle: "))
        if base <= 0:
            print("Invalid base. Base must be greater than 0.")
            continue

        height = int(input("Enter the height of the triangle: "))
        if height <= 0:
            print("Invalid height. Height must be greater than 0.")
            continue

        print(f"Triangle area = {0.5 * base * height}")
        break


def circle_area():
    while True:
        radius = int(input("Enter the radius of the circle: "))
        if radius <= 0:
            print("Invalid radius. Radius must be greater than 0.")
            continue
        else:
            return print(f"Circle area = {3.14 * (radius ** 2)}")


def rectangle_area():
    while True:
        width = int(input("Enter the width of the of the rectangular: "))
        if width <= 0:
            print("Invalid width. Width must be greater than 0.")
            continue
        length = int(input("Enter the length of the of the rectangular: "))
        if length <= 0:
            print("Invalid length. Length must be greater than 0.")
            continue
        else:
            return print(f"Rectangle area = {width * length}")


while True:
    selection = int(input("1. Sum\n"
                          "2. Subtract\n"
                          "3. Multiply\n"
                          "4. Division\n"
                          "5. Triangle area\n"
                          "6. Circle area\n"
                          "7. Rectangle area\n"
                          "8. Exit\n"))
    while True:
        if selection >= 1 and selection <= 8:
            break
        else:
            selection = int(input("Invalid Input :( Please try a number in between 1-8 "))
    if selection == 1:
        add()
        print("---------------------------------------------")
    elif selection == 2:
        subtract()
        print("---------------------------------------------")
    elif selection == 3:
        multiply()
        print("---------------------------------------------")
    elif selection == 4:
        division()
        print("---------------------------------------------")
    elif selection == 5:
        triangle_area()
        print("---------------------------------------------")
    elif selection == 6:
        circle_area()
        print("---------------------------------------------")
    elif selection == 7:
        rectangle_area()
        print("---------------------------------------------")
    elif selection == 8:
        print("Bye Bye, Have a nice day ^_^")
        exit()
