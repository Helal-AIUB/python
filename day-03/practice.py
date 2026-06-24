# marks = [39, 87, 90, 56, 34, 45, 67, 23,90]
# print(marks)
# print(type(marks))
# print(len(marks))

# strings in python is immutable but list in python is mutable that means list data can be changable but string not
# str = "hello"
# str[1] = "a"   # not possible

# str2 = ["name", "roll", "class", "phone"]
# str2[2]= "marks"
# print(str2)


# List Slicing
# student = ["karim", 78, "k@gmail.com", 23, "cricket"]
# print(student)
# print(student[0:2])
# print(student[:4])
# print(student[-3:])

#-----------------------------------------Methods in Python---------------------------------------

# Methods of List
# student = ["karim", 78, "karim@gmail.com", "Badda"]
# student.append("018....")
# student.remove(78)
# student.reverse()
# print(student)


# list = [23,2,56,12,34,23]
# list.sort()
# list.append(100)
# print(list)
# list.sort(reverse = True)
# print(list)

# list =["banana","g@gmail.com", "age", "@abc"]
# list.sort()
# print(list)

# list = [3,2,5,4,6,9,7]
# list.insert(2,10);
# print(list)


# list = [3,2,5,4,6,9,7]
# list.remove(5);
# print(list)


# list = [3,2,5,4,6,9,7]
# list.pop(1);
# print(list)

#----------------------------- Tuples in Python---------------------------

# tuple = (12,15,13,11,40,20)
# print(type(tuple))
# print(tuple)
# print(tuple[0])
# print(tuple[1])

# tup = 1, 2, 3,4 ,5
# print(len(tup))
# print(type(tup))
# print(tup)

# Tuple Slicing also possible
# tup = 1, 2, 3,4 ,5
# print(tup[1:4])

#------------------------------Methods in Tuples---------------------------

# tuple = (1,4,6,2,3,4,2)
# print(tuple.index(2))
# print(tuple.count(2))


#------------------------------Practice Questions---------------------------

# ask user to input 3 movies name and store them into a list
# movies = []
# mov1 = input("Enter 1st movie name: ")
# mov2 = input("Enter 2nd movie name: ")
# mov3 = input("Enter 3rd movie name: ")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# fruits = []
# fruits.append(input("Enter first fruits name: "))
# fruits.append(input("Enter second fruits name: "))
# fruits.append(input("Enter 3rd fruits name: "))
# print(fruits)


#Whether a list is palindrome or not?
# list = []
# list.append(input("Enter a value: "))
# list.append(input("Enter a value: "))
# list.append(input("Enter a value: "))
# list_copy = list.copy()
# list_copy.reverse()
# if(list == list_copy):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# list = ["r","a","c","e","c","a","r"]
# list_copy = list.copy()
# list_copy.reverse()
# if(list == list_copy):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# tuple = ("A","B","C","A","D","A","B")
# print(tuple.count("A"))


# list = []
# list.append(input("Enter Grade: "))
# list.append(input("Enter Grade: "))
# list.append(input("Enter Grade: "))
# list.append(input("Enter Grade: "))
# list.append(input("Enter Grade: "))
# list.append(input("Enter Grade: "))

# print(list.count("A+"))
# list.sort()
# print("list are: ",list)


# list = [12,13,24,35]
# list[1] = 30
# print(list)

tuple = (12,11,15)
tuple[0] = 30
print(tuple)


