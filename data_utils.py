#! /usr/bin/env python3
import csv
from datetime import datetime, time

FILENAME = "students.csv"
current_time = datetime.now().time()

"""
author: Imraan Arbab
date: August 13, 2023
desc: This module contains the functions that access the csv files, and it contains the methods that will register
the user's needs such as dropping a course, registering for a course, displaying the course list, etc.
"""
def display_menu1():
    """
    This displays the menu to the screen and displays the list of options that the user can do.
    """
    print("info     - Student information")
    print("list     - Course listing")
    print("detail   - Course detail")
    print("register - Register for a class")
    print("drop     - Drop class")
    print("menu     - Menu")
    print("exit     - Exit")
    print()

def read_students():
    """
    This reads the students csv file, and returns the contents of the file as list back to the calling function
    :return: The contents of the students csv file is returned as a list
    """
    students = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            students.append(row)
    return students

def read_courses(file_path):
    """
    This reads the courses csv file, and returns the contents of the file as list back to the calling function
    :return: The contents of the courses csv file is returned as a list
    """
    courses = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')
        for row in reader:
            if len(row) == 7:
                course_id, course_code, course_name, credit_hours, day, time, instructor = row
                course = {
                    'course_id': int(course_id.strip()),
                    'course_code': course_code.strip(),
                    'course_name': course_name.strip(),
                    'credit_hours': float(credit_hours.strip()),
                    'day': day.strip(),
                    'time': time.strip(),
                    'instructor': instructor.strip()
                }
                courses.append(course)
    return courses

def write_students(students):
    """
    This writes content to the students csv file, and the students csv file is updated
    :param students: This is the name of the file that is passed in and the file we are writing to
    """
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(students)

def display_menu():
    """
    This displays the initial menu to the screen
    """
    print("Saddleback College Registration")
    print()

def read_registrations(file_path):
    """
    This reads the courses csv file, and returns the contents of the file as list back to the calling function
    :return: The contents of the courses csv file is returned as a list
    """
    registrations = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')
        for row in reader:
            if len(row) == 2:
                username, registration_id = row
                registration = (username.strip(), int(registration_id.strip()))
                registrations.append(registration)
    return registrations

def time_calculation(student, current_time):
    """
    This calculates the time of the day and greets the user based on the time of the day
    :param student: This is the name of the user that is accessing the program
    :param current_time: This is the current time that the user is accessing the program
    """
    if current_time >= time(0, 0) and current_time < time(12, 0):
        print()
        print(f"Good Morning, {student[2].title()}, what would you like to do today?")
        print()
        display_menu1()
    elif current_time >= time(12, 0) and current_time < time(17, 0):
        print()
        print(f"Good Afternoon, {student[2].title()}, what would you like to do today?")
        print()
        display_menu1()
    else:
        print()
        print(f"Good Evening, {student[2].title()}, what would you like to do today?")
        print()
        display_menu1()

def find(student_names, student_id):
    """
    This takes the list of the students, anda student id entered by the user and checks if the id entered is
    a valid student id
    :param student_names: This is the list of the students that we are searching in.
    :param student_id: This is the student id that is entered by the user, and that we are validating
    """
    found = False
    for student in student_names:
        if student[0].lower() == student_id.lower():
            time_calculation(student, current_time)
            found = True
            break
    if not found:
        print(f"{student_id} was not found.\n")

def write_registrations(student):
    """
    This writes content to the registration csv file, and the registration csv file is updated
    :param student: This is the student we are registering and adding to the csv file
    """
    with open("registration.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(student)

def generate_student_id(first_name, last_name, existing_ids):
    """
    This generates a random student id for a new student added to the csv file.
    If the user enters the same name that is found in the csv file , the digit in their
    username is incremented so the same id is not used for two students
    :param first_name: This is the first name of the student
    :param last_name: This is the last name of the student
    :param existing_ids: This is the ids of the existing students
    :return: The unique id is returned to the calling function
    """
    number = 0
    student_id = f"{first_name[0]}{last_name}{number}"
    while student_id in existing_ids:
        number += 1
        student_id = f"{first_name[0]}{last_name}{number}"
    return student_id

def add(first_name, last_name, students):
    """
    This adds a student to the students csv file. The first name, and last name (entered)
    by the user is combined with a digit to create a unique student id, and the student is
    added to the students list
    :param first_name: This is the first name of the student
    :param last_name: This is the first name of the student
    :param students: This is the list of the students
    """
    existing_ids = [student[0] for student in students]
    student_id = generate_student_id(first_name, last_name, existing_ids)
    student = (student_id, first_name, last_name)
    students.append(student)
    write_students(students)
    print(f"Student {student_id.lower()} has been added.")
    time_calculation(student, current_time)

def info(students, registration_info, student_id, courses):
    """
    This displays the information of a specific student, and the courses the student is
    registered for.
    :param students: This is the list of the students
    :param registration_info: This is the courses that each student is registered for
    :param student_id: This is the student id of the individual student
    :param courses: This is the list of courses available for registration
    """
    student_courses = []
    total_units = 0
    student_name = ""

    # Find the student's registered courses
    for student in students:
        if student[0] == student_id:
            student_name = f"{student[1]}, {student[2]}"
            break

    # If the student name exists
    if student_name:
        for registration in registration_info:
            # Checks if element matches student id
            if registration[0] == student_id:
                # Course id extracted from registration and assigned to course id variable
                course_id = registration[1]
                for course in courses:
                    # Check if the course ids match with one another
                    if course['course_id'] == course_id:
                        student_courses.append(course)
                        total_units += course['credit_hours']

        # Display student information
        print(f"Student id: {student_id}")
        print(student_name)
        print("Registered Courses")

        # Display the list of courses
        print("Ticket   Code     Course Name                                 Units   Day   Time          Instructor")
        print("===========================================================================================================")
        for course in student_courses:
            print(
                f"{course['course_id']:<9}{course['course_code']:<9}{course['course_name']:<45}{course['credit_hours']:>5.1f}  {course['day']:<6}{course['time']:<14}{course['instructor']:<15}")

        # Display the total line
        print(str(len(student_courses)) + " Course(s) Registered")
        print(f"                                                        Units: {total_units:>5.1f}")
    else:
        print(f"{student_id} was not found.\n")

def detail(courses, registration_info, students):
    """
    This displays the information of a specific course such as the instructor, the number of
    units, and it displays the students that are registered for the course.
    :param courses: This is the list of the courses
    :param registration_info: This is the courses that each student is registered for
    :param students: This is the list of the students
    """
    while True:
        ticket_number = input("Enter course ticket # (or 'exit'): ")
        if ticket_number.lower() == "exit":
            return

        found = False
        for course in courses:
            # Checking if the ticket numbers match
            if str(course['course_id']) == ticket_number:
                # Printing the course details
                print()
                print(f"Code: {course['course_code']} Course Name: {course['course_name']}")
                print(f"Units: {course['credit_hours']} Day: {course['day']} Time: {course['time']}")
                print(f"Instructor: {course['instructor']}")
                print("===================================")
                registered_students = []
                for registration in registration_info:
                    # Checking if the course ids match with one another
                    if registration[1] == course['course_id']:
                        # Student id is extracted
                        student_id = registration[0]
                        for student in students:
                            # If the student id in registration matches the student id
                            # of the current student, then the student is registered
                            if student[0] == student_id:
                                registered_students.append(student)
                                break
                if registered_students:
                    for student in registered_students:
                        # Formatting according to the specifications in the assignment
                        student_id = student[0].ljust(13)
                        last_name = student[2].ljust(16)
                        first_name = student[1].ljust(11)
                        print(f"{student_id}{first_name}{last_name}")
                    print(f"Total Students Registered: {len(registered_students)}")
                else:
                    print("No students registered for this course.")
                found = True
                break

        if not found:
            print(f"{ticket_number} not found.")

        print()
        break


def register(students, student_id, registration_info, courses):
    """
    This allows a student to register for a course and ensures that the ticket number
    entered is valid. The function goes through a variety of checks such as class size,
    unit limit, etc. to ensure that the student is able to register for the course.
    :param students: This is the list of the students
    :param student_id: This is the student id of the student registering for the course
    :param registration_info: This is the courses that each student is registered for
    :param courses: This is the list of the courses
    """
    total_units = 0
    student_courses = []
    student_name = ""

    # Calculating the total number of units before registering for a course
    for student in students:
        # Find a matching student id
        if student[0] == student_id:
            student_name = f"{student[1]}, {student[2]}"
            break

    if student_name:
        for registration in registration_info:
            # If a matching student id is found in the list of registered students
            if registration[0] == student_id:
                course_id = registration[1]
                for course in courses:
                    if course['course_id'] == course_id:
                        student_courses.append(course)
                        total_units += course['credit_hours']

    while True:
        print("Enter ticket # or 'exit'")
        ticket_number = input("Enter course ticket # (or 'exit'): ")
        if ticket_number.lower() == "exit":
            print()
            return

        found = False
        for course in courses:
            if str(course['course_id']) == ticket_number:
                # Checking if the class limit does not exceed 15
                if sum(1 for reg in registration_info if str(reg[1]) == ticket_number) > 15:
                    print(f"{ticket_number} is full.")
                    print()
                    return

                total_units += course['credit_hours']

                # Checking if the total number of units that the student is registered
                # for does not exceed 12
                if total_units > 12:
                    print(f"Cannot register for {ticket_number}. Exceeds maximum unit limit.")
                    print()
                    return

                # Checking if the student has already registered for this course
                for student in registration_info:
                    # Checking the ticket number entered
                    if str(student[1]) == ticket_number:
                        # Checking the student id of the student in the registered list
                        # and the current list
                        if str(student[0]) == student_id:
                            print(f"{student_id} is already registered for this course.")
                            print()
                            return
                        else:
                            print(f"Another student is already registered for this course.")
                        found = True
                        break

                if not found:
                    # Student is registered after all the checks
                    registration_info.append((student_id, ticket_number))
                    # Updating the registration csv file
                    write_registrations(student_id)
                    print(f"{student_id} was added to {ticket_number}.")
                    print()
                    return
                break

        if not found:
            print(f"{ticket_number} not found.")

        print()

def drop(students, student_id, registration_info, courses):
    """
    This allows a student to drop a course and ensures that the ticket number
    entered is valid.
    :param students: This is the list of the students
    :param student_id: This is the student id of the student dropping the course
    :param registration_info: This is the courses that each student is registered for
    :param courses: This is the list of the courses
    """
    while True:
        print("Enter ticket # or 'exit'")
        ticket_number = input("Enter course ticket # (or 'exit'): ")
        if ticket_number.lower() == "exit":
            print()
            return

        found = False
        for i, course in enumerate(courses):
            # If a matching course is found, the student is dropped from the course
            if str(course['course_id']) == ticket_number:
                print(f"{student_id} was dropped from {ticket_number}.")
                found = True
                for j, reg in enumerate(registration_info):
                    # If a matching entry in teh registered students is found with the
                    # same student id and ticket number, the entry is removed from the
                    # list
                    if reg[0] == student_id and reg[1] == ticket_number:
                        registration_info.pop(j)
                        print(f"{student_id} was dropped from {ticket_number}.")
                        # Updating the registration file information
                        write_registrations(student_id)
                        break
                break

        if not found:
            print(f"{ticket_number} not found.")
        else:
            break

    print()

def list(courses):
    """
    This displays all the courses available for registration and lists the details of
    each course
    :param courses: This is the list of the courses.
    """
    i = 1
    print()
    print("Course Listing by Ticket")
    print("Ticket   Code     Course Name                                 Units   Day   Time          Instructor")
    print("===================================================================================================")

    # Sort courses by ticket number
    sorted_courses = sorted(courses, key=lambda x: x['course_id'])

    for course in sorted_courses:
        i += 1
        print(
            f"{course['course_id']:<9}{course['course_code']:<9}{course['course_name']:<45}{course['credit_hours']:>5.1f}  {course['day']:<6}{course['time']:<14}{course['instructor']:<15}")

    # Display the total line
    print(str(i) + " Courses")
    print()


