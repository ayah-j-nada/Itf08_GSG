def square ():
    x = int(input("Enter the length of the side of the square: "))

    area = x ** 2
    perimeter = 4 * x

    print(f"Square Area = {area}")
    print(f"Square Perimeter = {perimeter}")

square()

def triangle():
    base = int(input("Enter the base length of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    side1 = int(input("Enter the length of side 1: "))
    side2 = int(input("Enter the length of side 2: "))
    side3 = int(input("Enter the length of side 3: "))

    area = 0.5 * base * height
    perimeter = side1 + side2 + side3

    print(f"Triangle Area = {area}")
    print(f"Triangle Perimeter = {perimeter}")

triangle()


