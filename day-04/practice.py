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

info = {
    "Name" : "ABC",
    "learning" : "Python",
    "topics" : ("doct","set"),
    "age" : 34,
    "marks" : [12,34,56,34],
    "is_audult" : True,
    12.99 : 99,
}


#keys() method

# print(len(info))
# print(list(info.keys()))     #type casting to list
# print(info.keys())


# print(info.values())
# print(info.items())
print(info.get("is_audult"))