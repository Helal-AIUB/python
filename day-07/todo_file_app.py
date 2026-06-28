import os
def add_task():
    task = input("Enter the task: ")
    try:
        if not os.path.exists("todos.txt") or os.path.getsize("todos.txt") == 0:
            with open("todos.txt", "w") as f:
                f.write(task)
        else:
            with open("todos.txt", "a") as f:
                f.write(", " + task)

        print("Task added successfully!")

    except Exception as e:
        print("Error:", e)

def view_tasks():
    try:
        with open("todos.txt", "r") as f:
            data = f.read()

            if data.strip() == "":
                print("No tasks available.")
                return

            tasks = data.split(",")

            print("\n------ Todo List ------")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i].strip()}")

    except FileNotFoundError:
        print("No todo file found.")

def delete_task():
    try:
        with open("todos.txt", "r") as f:
            data = f.read()

        tasks = [task.strip() for task in data.split(",") if task.strip()]   # string to list

        if len(tasks) == 0:
            print("No tasks available.")
            return

        print("\n------ Todo List ------")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")

        number = int(input("Enter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        removed = tasks.pop(number - 1)

        with open("todos.txt", "w") as f:
            f.write(", ".join(tasks))     # list to string

        print(f'"{removed}" deleted successfully!')

    except FileNotFoundError:
        print("No todo file found.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n====== TODO MENU ======")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        view_tasks()

    elif choice == "2":
        add_task()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-4.")