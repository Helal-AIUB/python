marks = int(input("Enter your Marks: "))
if((marks > 100) or (marks < 0)):
    grade = "Invalid Marks. Please enter marks between 0 and 100"
elif(marks >= 80):
    grade = "A+"
elif(marks >= 70):
    grade = "A"
elif(marks >= 60):
    grade = "A-"
elif(marks >= 50):
    grade = "B"
elif(marks >= 40):
    grade = "C"
else:
    grade = "Fail"
print(grade)