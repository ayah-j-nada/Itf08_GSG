name = input("Enter your full name: ")
mobile = input("Enter yor mobile number (05x-xxxx-xxx):  ")
year_of_birth = int(input("Enter your year of birth: "))
user_age = 2023 - year_of_birth
print(f"Name: {name}")
print(f"Age: {user_age}")
mobile = mobile.split("-")
print(f"Mobile: {mobile}")

