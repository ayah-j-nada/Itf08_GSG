persons = []


def load_data():
    with open('info.txt', "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line = line.split("|")
            new_person = {
                "user_name": line[0],
                "age": line[1],
                "dob": line[2]
            }
            persons.append(new_person)
    print("Data Loaded Successfully")
    return persons


def update_data(data: list):
    data_str = []
    for i in data:
        i = f"{i.get('user_name')}|{i.get('age')}|{i.get('dob')}\n"
        data_str.append(i)
    with open('info.txt', "a") as file:
        file.writelines(data_str)
        file.close()


while True:
    selection = int(input("1. Add New Person\n"
                          "2. Exit"))
    if selection == 1:
        user_name = input("Enter your User Name: ")
        age = input("Enter your Age: ")
        date_of_birth = input("Enter your Date Of Birth: ")
        person = {
            "user_name": user_name,
            "age": age,
            "dob": date_of_birth
        }
        persons.append(person)
        update_data(persons)
        print("New Person Added Successfully.\n")

    elif selection == 2:
        exit()
    else:
        print("Invalid Input.\n")
