def rectangular():
    width = int(input("Enter the width of the of the rectangular: "))
    length = int(input("Enter the length of the the rectangular : "))

    area = length * width
    perimeter = (2 * length) + (2 * width)

    if area >= 10:
        print("The area is larger than or equal 10")
    elif 0 < area < 10:
        print("The area is smaller than 10")
    else:
        print("invalid input")

    print(f"Rectangular Area = {area}")
    print(f"Rectangular Perimeter = {perimeter}")


rectangular()


def triangle():
    """Function to get triangle area and perimeter"""
    base = int(input("Enter the base length of the triangle: "))
    height = int(input("Enter the height of the triangle: "))
    side1 = int(input("Enter the length of side 1: "))
    side2 = int(input("Enter the length of side 2: "))
    side3 = int(input("Enter the length of side 3: "))

    area = 0.5 * base * height
    perimeter = side1 + side2 + side3
    if area >= 10:
        print("The area is larger than or equal 10")
    elif 0 < area < 10:
        print("The area is smaller than 10")
    else:
        print("invalid input")

    print(f"Triangle Area = {area}")
    print(f"Triangle Perimeter = {perimeter}")


triangle()


def circle():
    """Function to get circle area and perimeter"""
    r = int(input("Enter the radius of the circle: "))
    area = 3.14 * (r ** 2)
    perimeter = 2 * 3.14 * r
    if area >= 10:
        print("The area is larger than or equal 10")
    elif 0 < area < 10:
        print("The area is smaller than 10")
    else:
        print("invalid input")

    print(f"Circle Area = {area}")
    print(f"Circle Perimeter = {perimeter}")


circle()
