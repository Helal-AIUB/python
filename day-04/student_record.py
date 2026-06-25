students = []

# Add Student
def add_student():
    student = {
        "id": int(input("Enter ID: ")),
        "name": input("Enter Name: "),
        "email": input("Enter Email: "),
        "department": input("Enter Department: "),
        "cgpa": float(input("Enter CGPA: "))
    }

    students.append(student)
    print("Student added successfully!\n")


# View All Students
def view_students():
    if len(students) == 0:
        print("No students found.\n")
        return

    print("\n----- Student List -----")
    for student in students:
        print(student)
    print()


# Search Student by ID
def search_student():
    sid = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == sid:
            print("Student Found:")
            print(student)
            return

    print("Student not found.\n")


# Update Student Email
def update_email():
    id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == id:
            new_email = input("Enter New Email: ")
            student["email"] = new_email
            print("Email updated successfully!\n")
            return

    print("Student not found.\n")


# Delete Student
def delete_student():
    id = int(input("Enter Student ID: "))

    for student in students:
        if student["id"] == id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return

    print("Student not found.\n")


# Show Total Number of Students
def total_students():
    print("Total abc:",len(students),"\n")


# Main Menu
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Email")
    print("5. Delete Student")
    print("6. Show Total Number of Students")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_email()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        total_students()
    elif choice == "7":
        print("Program terminated.")
        break
    else:
        print("Invalid choice! Try again.\n")