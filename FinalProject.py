#! /usr/bin/env python3
import data_utils
"""
author: Imraan Arbab
date: August 13, 2023
desc: This module is the main module and it contains the menus and the functions that allow the user to perform a
variety of tasks such as as registering for a course, dropping a course, etc.
"""

def main():
    # Reading and initializing the data from the csv files
    data_utils.display_menu()
    registration_info = data_utils.read_registrations("registration.csv")
    courses = data_utils.read_courses("courses.csv")
    students = data_utils.read_students()

    while True:
        student_id = input(
            "Enter Student ID (or 'add' to add a new student, or 'exit' to exit the application): "
        )

        if student_id.lower() == "exit":
            print("Session ended.")
            break
        elif student_id.lower() == "add":
            # Creating a new student
            while True:
                try:
                    print()
                    last_name = input("Enter Student's Last Name: ")
                    first_name = input("Enter Student's First Name: ")
                    print()

                    if not last_name.isalpha() or not first_name.isalpha():
                        raise ValueError()

                    break
                except ValueError:
                    print("Student's name can only contain alphabetic letters and cannot be left blank.")

            data_utils.add(first_name, last_name, students)
        else:
            # Checking to see if the id entered is valid or not
            data_utils.find(students, student_id)

            while True:
                response = input("Enter your selection: ")

                if response.lower() == "info":
                    data_utils.info(students, registration_info, student_id, courses)
                elif response.lower() == "list":
                    data_utils.list(courses)
                elif response.lower() == "detail":
                    data_utils.detail(courses, registration_info, students)
                elif response.lower() == "register":
                    data_utils.register(students, student_id, registration_info, courses)
                elif response.lower() == "menu":
                    print()
                    data_utils.display_menu1()
                elif response.lower() == "exit":
                    print("Session ended.")
                    return
                elif response.lower() == "drop":
                    print()
                    data_utils.drop(students, student_id, registration_info, courses)
                else:
                    print("Invalid selection, please try again.")
                    print()


if __name__ == "__main__":
    main()
