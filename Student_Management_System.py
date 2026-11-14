# Student Management System
# BCA 1st Semester Python Assignment

students = []


# Main Program

def main():

    while True:

        print("STUDENT MANAGEMENT SYSTEM")

        print("1. Add Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Enter Marks")
        print("5. Calculate Grade")
        print("6. Calculate Attendance")
        print("7. Show Student Result")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            show_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            enter_marks()

        elif choice == "5":
            calculate_grade()

        elif choice == "6":
            calculate_attendance()

        elif choice == "7":
            show_result()

        elif choice == "8":
            print("Thank you for using the Student Management System.")
            break

        else:
            print("Wrong choice. Please try again.")


# Function to add a student

def add_student():

    print("Add Student")

    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    course = input("Enter course: ")
    semester = input("Enter semester: ")

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "semester": semester,
        "marks": [],
        "attendance": 0
    }

    students.append(student)

    print("Student added successfully!")


# Function to show all students

def show_students():

    print("Student List")

    if len(students) == 0:
        print("No student record available.")
        return

    for student in students:

        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Course:", student["course"])
        print("Semester:", student["semester"])

        if len(student["marks"]) > 0:

            total = sum(student["marks"])
            percentage = total / 5

            print("Total Marks:", total)
            print("Percentage:", percentage, "%")

        if student["attendance"] != 0:
            print("Attendance:", student["attendance"], "%")


# Function to search a student

def search_student():

    print("Search Student")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            print("Student Found")
            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Semester:", student["semester"])

            return

    print("Student not found.")


# Function to enter marks

def enter_marks():

    print("Enter Marks")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            marks = []

            for i in range(1, 6):

                mark = float(input("Enter marks of subject " + str(i) + ": "))

                marks.append(mark)

            student["marks"] = marks

            total = sum(marks)
            percentage = total / 5

            print("Marks saved successfully!")
            print("Total Marks:", total)
            print("Percentage:", percentage, "%")

            return

    print("Student not found.")


# Function to calculate grade

def calculate_grade():

    print("Calculate Grade")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            if len(student["marks"]) == 0:
                print("Marks are not entered yet.")
                return

            total = sum(student["marks"])
            percentage = total / 5

            print("Student Name:", student["name"])
            print("Total Marks:", total)
            print("Percentage:", percentage, "%")

            if percentage >= 90:
                grade = "A+"

            elif percentage >= 80:
                grade = "A"

            elif percentage >= 70:
                grade = "B"

            elif percentage >= 60:
                grade = "C"

            elif percentage >= 50:
                grade = "D"

            elif percentage >= 33:
                grade = "E"

            else:
                grade = "F"

            print("Grade:", grade)

            if percentage >= 33:
                print("Result: PASS")
            else:
                print("Result: FAIL")

            return

    print("Student not found.")


# Function to calculate attendance

def calculate_attendance():

    print("Attendance Calculator")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            total = int(input("Enter total lectures: "))
            attended = int(input("Enter attended lectures: "))

            if total == 0:
                print("Total lectures cannot be zero.")
                return

            if attended > total:
                print("Attended lectures cannot be greater than total lectures.")
                return

            attendance = (attended / total) * 100

            student["attendance"] = attendance

            print("Attendance:", attendance, "%")

            if attendance >= 75:
                print("Status: Eligible")
            else:
                print("Status: Not Eligible")

            return

    print("Student not found.")


# Function to show complete result

def show_result():

    print("Student Result")

    roll = input("Enter roll number: ")

    for student in students:

        if student["roll"] == roll:

            print("RESULT")

            print("Roll Number:", student["roll"])
            print("Name:", student["name"])
            print("Course:", student["course"])
            print("Semester:", student["semester"])

            if len(student["marks"]) > 0:

                total = sum(student["marks"])
                percentage = total / 5

                print("Total Marks:", total)
                print("Percentage:", percentage, "%")

                if percentage >= 90:
                    grade = "A+"

                elif percentage >= 80:
                    grade = "A"

                elif percentage >= 70:
                    grade = "B"

                elif percentage >= 60:
                    grade = "C"

                elif percentage >= 50:
                    grade = "D"

                elif percentage >= 33:
                    grade = "E"

                else:
                    grade = "F"

                print("Grade:", grade)

                if percentage >= 33:
                    print("Result: PASS")
                else:
                    print("Result: FAIL")

            else:
                print("Marks: Not entered")

            if student["attendance"] != 0:
                print("Attendance:", student["attendance"], "%")
            else:
                print("Attendance: Not entered")

            return

    print("Student not found.")


# Start the program

main()