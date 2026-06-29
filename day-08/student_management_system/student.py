class Student:

    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self):
        try:
            student = {
                "id": input("Enter ID: "),
                "name": input("Enter Name: "),
                "department": input("Enter Department: "),
                "cgpa": input("Enter CGPA: ")
            }

            self.students.append(student)
            print("Student Added Successfully!")

        except Exception as e:
            print("Error:", e)

    # View Students
    def view_students(self):
        if len(self.students) == 0:
            print("No Student Found!")
            return

        for student in self.students:
            print(student)

    # Search Student
    def search_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:
            if student["id"] == student_id:
                print(student)
                return

        print("Student Not Found!")

    # Update Student
    def update_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student["id"] == student_id:

                student["name"] = input("New Name: ")
                student["department"] = input("New Department: ")
                student["cgpa"] = input("New CGPA: ")

                print("Updated Successfully!")
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):
        student_id = input("Enter Student ID: ")

        for student in self.students:

            if student["id"] == student_id:
                self.students.remove(student)
                print("Deleted Successfully!")
                return

        print("Student Not Found!")

    # Save File
    def save_file(self):

        with open("data.txt", "w") as file:

            for student in self.students:

                line = f'{student["id"]},{student["name"]},{student["department"]},{student["cgpa"]}\n'

                file.write(line)

        print("Saved Successfully!")

    # Load File
    def load_file(self):

        try:

            with open("data.txt", "r") as file:

                self.students = []

                for line in file:

                    data = line.strip().split(",")

                    student = {
                        "id": data[0],
                        "name": data[1],
                        "department": data[2],
                        "cgpa": data[3]
                    }

                    self.students.append(student)

            print("Loaded Successfully!")

        except FileNotFoundError:
            print("No data file found!")