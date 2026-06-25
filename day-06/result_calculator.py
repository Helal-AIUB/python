def calculate_total(marks):
    return sum(marks)


def calculate_average(total, n):
    return total / n


def calculate_grade(average):
    if average >= 80:
        return "A+"
    elif average >= 70:
        return "A"
    elif average >= 60:
        return "A-"
    elif average >= 50:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"


def show_result(name, total, average, grade):
    print("\n----- Student Result -----")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average Marks:", average)
    print("Grade:", grade)

    if grade == "Fail":
        print("Status: Fail")
    else:
        print("Status: Pass")


# Main Program
name = input("Enter student name: ")

n = int(input("Enter number of subjects: "))

marks = []

for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

total = calculate_total(marks)
average = calculate_average(total, n)
grade = calculate_grade(average)

show_result(name, total, average, grade)