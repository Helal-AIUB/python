#----------------Whole file read---------------------
# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))

#----------------Only 5 character Read---------------------

# f = open("demo.txt","r")
# data = f.read(5)
# print(data)
# print(type(data))

#----------------Only first line read---------------------

# f = open("demo.txt","r")
# line1 = f.readline()
# print(line1)
# print(type(line1))

#----------------Two line read---------------------

# f = open("demo.txt", "r")

# line1 = f.readline()
# line2 = f.readline()

# print(line1)
# print(line2)

# f.close()

#---------------------Write in a File--------------
# f = open("demo.txt","w")
# f.write("something")
# f.close()

#---------------------------------Write on a File------------
# f = open("demo.txt", "w")
# f.write("I will learn Javascrift tomorrow. 123")
# f.close()

#---------Write(append) another line-----------
# f = open("demo.txt", "a")
# f.write("\n after that I will learn NodeJS")
# f.close()


#----------------------Create and write a file---------------------

# f = open("sample.txt","a")
# f.write("I created a sample.txt file bbbb")
# f.close()

#-----------------------read and write(first theke overwrite hoye jabe------

# f = open("demo.txt","r+")

# f.write("I am writing")
# f.close()

#-----------------------read and write(trancate-mane previous likha delete hoye jabe)------

# f = open("abc.txt","w+")

# f.write("I am writing")
# f.close()


#----------------------With Syntax----------------------------
# Read
# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)

# write - truncate

# with open("demo.txt", "w") as f:
#     f.write("New Data")
#     f.close()

#------------------------------DELETE A FILE-----------------------------
# import os
# os.remove("sample.txt")


#------------------------SOLVE PRACTICE QUESTION-------------------------------

# f = open("practice.txt","w")
# f.write("Hi Everyone. \nWe are learning File I/O.\nusing Java. \nI like programming in Java")
# f.close();

# with open("practice.txt","r") as f:
#     data = f.read()
    
# newData = data.replace("Java","Python")
# print(newData)

# with open("practice.txt","w") as f:
#     f.write(newData)

# Search world "learning" exists or not?

# word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word) == -1):
#         print("Not Found")
#     else:
#         print("Found")


# Search and print desire line number

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if(word in data):
#                 return line_no
#             line_no += 1
#     return -1

# print(check_for_line())


#  print Numbers separated by comma

# with open("abc.txt", "r") as f:
#     data = f.read()
#     # print(data)
#     # print(len(data))

#     num = ""
#     for i in range(len(data)):
#         if(data[i] == ","):
#             print(int(num))
#             num = ""
#         else:
#             num += data[i]



# Even Numbers count separated by comma
# count = 0
# with open("abc.txt", "r") as f:
#     data = f.read()
#     nums = data.split(",")
#     for val in nums:
#         if(int(val)%2 == 0):
#             count +=1
# print(count)
