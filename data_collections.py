students_count = int(input("Enter the number of students: "))
print("--------------------------------------------")

for i in range(0, students_count):
    marks_count = int(input(f"Enter the number of marks for student {i+1}: "))
    my_marks = []
    for j in range(0, marks_count):
        mark = float(input(f"Enter Mark {j+1}: "))
        my_marks.append(mark)

    average = sum(my_marks)/len(my_marks)
    average = round(average, 2)
    # print("Average = ", average)
    # print("Max Mark = ", max(my_marks))
    # print("Min Mark = ", min(my_marks))
    print(f""" 
    Average = {average}
    Max Mark = {max(my_marks)}
    Min Mark = {min(my_marks)}
    """)
    print("--------------------------------------------")
