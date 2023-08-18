# Question 1
def is_palindrome(number):
    number_str = str(number)
    if number_str == number_str[::-1]:
        return True
    else:
        return False


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


while True:
    selection = int(input("1. Check if a number is palindrome\n"
                          "2. Check if a number is even or odd\n"
                          "3. Exit"
                          ))
    while True:
        if selection >= 1 and selection <= 3:
            break
        else:
            selection = int(input("Invalid Input :( Please choose 1 or 2 "))
    if selection == 1:
        num = int(input("Enter a number: "))
        if is_palindrome(num):
            print("The number is a palindrome.")
        else:
            print("The number is not a palindrome.")
        print("---------------------------------------------")
    elif selection == 2:
        num = int(input("Enter a number: "))
        result = check_even_odd(num)
        print(f"The number is {result}.")
        print("---------------------------------------------")
    elif selection == 3:
        exit()

# Question 2
def list_smallest_largest(numbers):
    numbers.sort()
    smallest = numbers[0]
    largest = numbers[-1]
    return smallest, largest


num = [10, 70, 21, 9, 50, 1, 8]
smallest, largest = list_smallest_largest(num)
print(f"The smallest number is: {smallest}")
print(f"The largest number is: {largest}")
