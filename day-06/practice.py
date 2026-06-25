
#----------------------Function In Python-----------------------------
# def sum(a, b):
#     s = a + b
#     return s
# print(sum(2,3))


# def multiplication(a,b):
#     mult = a*b
#     # print(mult)
#     return mult
# print(multiplication(2,3))
# # multiplication(5,6)


# Average of 3 numbers
# sum = 0
# num = int(input("Enter a Number: "))
# sum +=num
# num = int(input("Enter a Number: "))
# sum +=num
# num = int(input("Enter a Number: "))
# sum +=num

# print("Average: ", sum/3)

# def Average(a, b, c):
#     sum = a + b + c
#     avg = sum / 3
#     return avg
# print(Average(20,30,40))


# cities = ["dhaka","barishal","chittagong","rongpur","cumilla","Mymansingh"]
# fruits = ["apple","banana","mango","orange","lichi"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(fruits)

# def print_list(list):
#     for item in list:
#         print(item, end=" ")
# print_list(fruits)


#----------------------------Factorial using Function-----------------
# def factorial(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *=i

#     print(fact)
# factorial(5)

#--------------------------USD to INR-----------------------
# def converter(usd):
#     return usd*83
# print(converter(2))


#---------------------------Recursion--------------------------------

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)


# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)
# res = fact(5)
# print(res)

# Calculate sum of first N number using recursion

# def addition(n):
#     if(n==0):
#         return 0
#     return addition(n-1) + n
# sum = addition(5)
# print(sum)



# print all list element using recursion
def print_list(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
cities = ["dhaka","khulna","barishal","cumilla"]
print_list(cities)