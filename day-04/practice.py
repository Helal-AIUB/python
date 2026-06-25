# info = {
#     "Name" : "ABC",
#     "learning" : "Python",
#     "topics" : ("doct","set"),
#     "age" : 34,
#     "marks" : [12,34,56,34],
#     "is_audult" : True,
#     12.99 : 99,
# }

# info["name"] = "Rozhan"

# print(info)
# print(type(info))
# print(info["name"])
# print(info["age"])
# print(info["topics"])
# print(info[12.99])


#-------------------------Nested Dictionaries------------------------

# student = {
#     "Name" : "Rahul",
#     "Subjects" : {
#         "phy" : 98,
#         "chem" : 78,
#         "math" : 99,
#     }
# }

# print(student["Subjects"])
# print(student["Subjects"]["chem"])

#-------------------------Methods in Dictionaries------------------------

# info = {
#     "Name" : "ABC",
#     "learning" : "Python",
#     "topics" : ("doct","set"),
#     "age" : 34,
#     "marks" : [12,34,56,34],
#     "is_audult" : True,
#     12.99 : 99,
# }


#keys() method

# print(len(info))
# print(list(info.keys()))     #type casting to list
# print(info.keys())


# print(info.values())
# print(info.items())
# print(info.get("is_audult"))
# info.update({"city":"Dhaka", "college": "AIUB",})

# newDict = {"country":"BD","capital":"dhaka"}
# info.update(newDict)
# print(info)

#-------------------------Sets in Python------------------------

# collection = {1,2,3,4,"Hello",56.5, 44}
# print(collection)
# print(len(collection))
# print(type(collection))

# collection = {}  # empty dictionary
# collection2 = set()  # empty set
# print(type(collection))
# print(type(collection2))


#-------------------------Methodss in Set------------------------

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.remove(2)
# print(collection)

# collection.clear()
# print(len(collection))


# collection = {"abc","world","hello","python","C++"}
# print(collection.pop())
# print(collection.pop())
# print(collection.pop())


# Set Union Example
# set1 = {1,2,3}
# set2 = {2,3,4,5}
# print(set1.union(set2))
# print(set1.intersection(set2))



#-------------------------Practice Question------------------------

# dict = {
#     "table" : ["A furniture", "fact and figures"],
#     "cat" : "A animal",
# }

# print(dict)


# collection = {
#     "Python", "Java", "C++", "Python", "C","Java", "C", "JS","JS"
# }
# print(len(collection))


# marks = {}
# x = int(input("Enter Phy marks: "))
# marks.update({"phy": x})

# x = int(input("Enter math marks: "))
# marks.update({"math": x})

# x = int(input("Enter eng marks: "))
# marks.update({"eng": x})

# print(marks)


values = { "9.0", 9}
print(values)

values2 = {
    ("float", 9.0),
    ("int", 9)
}
print(values2)