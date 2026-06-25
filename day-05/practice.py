# i = 1
# while i<=5:
#     print("Hello")
#     i +=1


# count = 1
# while count <= 5:
#     print(count)
#     count +=1
# print("loop ended")


# count = 5
# while count >= 1:
#     print(count)
#     count -=1
# print("loop ended")


#Multiplication table 

# n = int(input("Enter a number: "))

# i = 1
# while i<=10:
#     print(n," X ",i," = ", n*i)
#     i +=1


# print number froma list

# list = [1,3,5,7,9,11,13,15,17,19]

# i=0
# while i < len(list):
#     print(list[i], end=" ")
#     i +=1

# Search a number in a tuple using loop

# tuple = (2,4,6,8,10,12,14,16,18,20)
# num = int(input("Enter a Number: "))
# idx = 0
# flag = False
# while idx < len(tuple):
#     if(tuple[idx]==num):
#         flag = True
#     idx +=1
# if(flag):
#     print("You Search: ",num," (Found)")
# else:
#     print("Not Found")



# --------------------------------FOR LOOP----------------------------------------

# list = [2,5,3,6,8,3,34,7]
# for i in list:
#     print(i, end=" ")


# print(range(5))

# seq = range(5)
# for i in seq:
#     print(i)


# for i in range(10):     # range(stop)
#     print(i)

# for i in range(2,10):     # range(start, stop)
#     print(i)

# for i in range(2,10,2):     # range(start, stop, step)
#     print(i)


# for i in range(100, 0, -1):
#     print(i)


# Sum of first n Numbers using White

# n = int(input("Enter a number: "))
# sum = 0
# count = 0
# while count<n:
#     print("Enter Number(",count+1,"): ")
#     num = int(input())
#     sum += num
#     count +=1
# print("Sum: ", sum)




# Factorial of first n numbers using for Loop

n = int(input("Enter a Number: "))
sum = 1
for i in range(n,0,-1):
    sum *= i
print("Factorial of ",n," :", sum)