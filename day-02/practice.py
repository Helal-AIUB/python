# str1 = "This is a string."
# str2 = 'This is also a string.'
# str3 = """This is also a string"""
# print(str1)
# print(str2)
# print(str3)

# Escape Sequence
# str = "This is a string. \nWe are creating it in python"    # Escape Sequence
# str2 = "This is a string. \tWe are creating it in python"
# print(str)
# print(str2)


# String Concatenation
# str1 = "Apna"
# print(str1, len(str1))
# str2 = "College"
# str = str1 + str2
# print(str)
# print(len(str))

# Indexing
# str = "Hello World"
# print(str[4])   #access


# Slicing
# str = "Apna College"
# print(str[1:4])
# print(str[5:len(str)])
# print(str[2:])
# print(str[:4])

# Negative Index
# str = "Apple"
# print(str[-4:-2])
# print(str[-5:])
# print(str[:-1])


# String Function
# str = "I am am am a Coder."
# print(str.endswith("er."))
# print(str.capitalize())
# print(str.replace("I am", "I'm"))
# print(str.find("Coder"))
# print(str.find("z"))
# print(str.count("am"))


# Video Practice Task
# name = input("Enter your First Name: ")
# print("Your first name length: ", len(name))

# name = input("Enter a string: ")
# print("(I) belongs to ", name.count("I")," times in that string")

# doller = input("Enter something: ")
# print("Doller($) belongs to ", doller.count("$")," times in that string")


# # Practice Even or Odd
# num = int(input("Enter a Number: "))
# if(num % 2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")

# practice greatest number among 3 number
# num1 = int(input("Enter Number One: "))
# num2 = int(input("Enter Number Two: "))
# num3 = int(input("Enter Number Three: "))
# if(num1 > num2 and num1 > num3):
#     print("number1(",num1,") is the greatest number")
# elif(num2 > num1 and num2 > num3):
#     print("number2(",num2,") is the greatest number")
# else:
#     print("number3",num3,") is the greatest number")

# practice a number multiple of 7 or not?
# num = int(input("Enter a Number:"))
# if(num%7==0):
#     print(num,"is the multiple of 7")
# else:
#     print(num,"is not multiple of 7")


text = ' aMr '
print(text.upper())
print(text.lower())
print(text.strip())

fruits = "apple, banana, mango, orange"
print(fruits.split())
