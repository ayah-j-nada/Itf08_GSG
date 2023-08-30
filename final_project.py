"""ITF 08 Final Project
#TODO 1 Enter your name and submission date
Name : Ayah Jamal-Edin Hussein Abu Nada
Delivery Date : 30-08-2023
Eng.Mohanad Alkrunz
"""
import random


# TODO 2 Define Course Class and define constructor with (course_id generated ,course name (user_input) and course mark
class Course:
    def __init__(self, course_name, course_mark):
        self.course_id = random.randint(1000, 9999)
        self.course_name = course_name
        self.course_mark = course_mark


class Student:
    # TODO 3 define static variable indicates total student count
    students_count = 0

    # TODO 4 define a constructor which includes
    # student_id (unique using random module)
    # student_name (user input)
    # student_age (user_inout)
    # student_number (user_input)
    # courses_list (List of Course Objects)
    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(10000000, 99999999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []
        Student.students_count += 1

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_course(self, course_name, course_mark):
        course = Course(course_name, course_mark)
        self.courses_list.append(course)
        self.save_student_data()

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for course in self.courses_list:
            print(f"Course Name: {course.course_name} | Course Mark: {course.course_mark}")

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        total_marks = 0
        for course in self.courses_list:
            total_marks += course.course_mark
        student_average = total_marks / len(self.courses_list)
        return student_average

    def save_student_data(self):
        with open("student.txt", "a") as file:
            file.write(f"{self.student_id}|{self.student_name}|{self.student_age}|{self.student_number}|")
            for course in self.courses_list:
                file.write(f"{course.course_name}|{course.course_mark}|")
            file.write("\n")


# in Global Scope
# TODO 8 declare empty students list

students = []

while True:

    # TODO 9 handle Exception for selection input
    selection = int(input("1.Add New Student\n"
                          "2.Delete Student\n"
                          "3.Display Student\n"
                          "4.Get Student Average\n"
                          "5.Add Course to student with mark.\n"
                          "6.Exit"
                          ))
    while True:
        if 1 <= selection <= 6:
            break
        else:
            selection = int(input("Invalid Input :( Please try a number in between 1-6 "))
    if selection == 1:
        while True:
            try:
                student_number = int(input("Enter Student Number: "))
                break
            except ValueError:
                print("Invalid Value")
        while True:
            student_name = input("Enter Student Name: ")
            if not student_name.isalpha():
                print("Invalid input. Student Name must contain alphabetic characters only.")
            else:
                break
        while True:
            try:
                student_age = int(input("Enter Student Age: "))
                break
            except ValueError:
                print("Invalid Value")
        # TODO 10 create student object and append it to students list
        student = Student(student_name, student_age, student_number)
        students.append(student)
        student.save_student_data()
        print("Student Added Successfully")
        print("--------------------------------------------------------------")

    elif selection == 2:
        while True:
            try:
                student_number = int(input("Enter Student Number: "))
                break
            except ValueError:
                print("Invalid Value")
        # TODO 11 find the target student using loops and delete it if exist , if not print ("Student Not Exist")
        for student in students:
            if student.student_number == student_number:
                students.remove(student)
                print(f"Student with number {student_number} deleted successfully")
                print("--------------------------------------------------------------")
                break
        else:
            print(f"Student with number {student_number} Not Exist")
            print("--------------------------------------------------------------")
    elif selection == 3:
        while True:
            try:
                student_number = int(input("Enter Student Number: "))
                break
            except ValueError:
                print("Invalid Value")
        # TODO 12 find the target student using loops and print student details  if exist , if not print ("Student
        #  Not Exist")
        for student in students:
            if student.student_number == student_number:
                student_dict = student.get_student_details()
                print("Student Details:")
                for key, value in student_dict.items():
                    if key == 'courses_list':
                        continue
                    print(f"{key}: {value}")

                print("Courses:")
                for course in student.courses_list:
                    print(f"Course Name: {course.course_name} | Course Mark: {course.course_mark}")
                break
        else:
            print(f"Student with number {student_number} Not Exist")
            print("--------------------------------------------------------------")
    elif selection == 4:
        while True:
            try:
                student_number = int(input("Enter Student Number: "))
                break
            except ValueError:
                print("Invalid Value")
        # TODO 13 find the target student using loops and get student average  if exist , if not print ("Student Not
        #  Exist")
        for student in students:
            if student.student_number == student_number:
                print(student.get_student_average())
                break
        else:
            print(f"Student with number {student_number} Not Exist")
            print("--------------------------------------------------------------")
    elif selection == 5:
        student_number = int(input("Enter Student Number: "))
        # TODO 14 ask user to enter course name and course mark then create course object then append it to target
        #  student courses
        course_name = input("Enter Course Name: ")
        course_mark = int(input("Enter Course Mark: "))
        course = Course(course_name, course_mark)
        for student in students:
            if student.student_number == student_number:
                student.courses_list.append(course)
                student.save_student_data()
                print("Course Enrolled Successfully")
                print("--------------------------------------------------------------")
                break
        else:
            print(f"Student with number {student_number} Not Exist")
            print("--------------------------------------------------------------")
    else:
        # TODO 15 call a function to exit the program
        exit()
