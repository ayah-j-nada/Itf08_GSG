def rectangular_area():
    w = int(input("Enter the width of the of the rectangular: "))
    l = int(input("Enter the length of the the rectangular : "))

    area = l * w

    print(f"Rectangular Area = {area}")

    if area >= 10:
        print("The area is larger than or equal 10")
    elif 0 < area < 10:
        print("The area is smaller than 10")
    else:
        print("invalid input")

rectangular_area()

def triangle_area():
    base = int(input("Enter the base length of the triangle: "))
    height = int(input("Enter the height of the triangle: "))

    area = 0.5 * base * height

    print(f"Triangle Area = {area}")

    if area >= 10:
        print("The area is larger than or equal 10")
    elif 0 < area < 10:
        print("The area is smaller than 10")
    else:
        print("invalid input")

triangle_area()

def circle_area():
    r = int(input("Enter the radius of the circle: "))
    area = 3.14 * (r**2)

    print(f"Circle Area = {area}")

    if area >= 10:
        print("The area is larger than or equal 10")
    elif 0 < area < 10:
        print("The area is smaller than 10")
    else:
        print("invalid input")

circle_area()

