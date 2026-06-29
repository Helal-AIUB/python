from student import Student

obj = Student()

while True:

    print("\n===== Student Management System =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Load Data")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        obj.add_student()

    elif choice == "2":
        obj.view_students()

    elif choice == "3":
        obj.search_student()

    elif choice == "4":
        obj.update_student()

    elif choice == "5":
        obj.delete_student()

    elif choice == "6":
        obj.save_file()

    elif choice == "7":
        obj.load_file()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")